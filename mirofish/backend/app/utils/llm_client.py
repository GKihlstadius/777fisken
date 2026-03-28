"""
LLM client wrapper
Unified OpenAI-format API calls with automatic model fallback chain:
  1. Primary model (e.g. 70B)
  2. Same-provider alternate model (e.g. Scout 17B — separate quota)
  3. Fallback provider (e.g. OpenRouter)
Includes retry logic for free-tier rate limits.
"""

import json
import logging
import os
import re
import time
from typing import Optional, Dict, Any, List
from openai import OpenAI

from ..config import Config

logger = logging.getLogger(__name__)

MAX_RETRIES = 6
RETRY_DELAY_SECONDS = 45

# Groq model fallback chain — each model has separate daily quota
# Model fallback chain — only used for Groq provider
GROQ_MODEL_FALLBACK_CHAIN = [
    "meta-llama/llama-4-scout-17b-16e-instruct",
    "llama-3.3-70b-versatile",
    "openai/gpt-oss-120b",
]


class LLMClient:
    """LLM client with automatic model and provider fallback"""

    def __init__(
        self,
        api_key: Optional[str] = None,
        base_url: Optional[str] = None,
        model: Optional[str] = None
    ):
        # Primary provider configuration
        eff_key, eff_url, eff_model = Config.get_effective_llm_config()
        self.api_key = api_key or eff_key
        self.base_url = base_url or eff_url
        self.model = model or eff_model

        if not self.api_key:
            raise ValueError("LLM API key not configured (set PRIMARY_LLM_API_KEY or LLM_API_KEY in .env)")

        self.client = OpenAI(
            api_key=self.api_key,
            base_url=self.base_url
        )

        # Fallback provider configuration (different provider, e.g. OpenRouter)
        fb_key, fb_url, fb_model = Config.get_fallback_llm_config()
        self.fallback_client = None
        self.fallback_model = fb_model
        if fb_key:
            self.fallback_client = OpenAI(
                api_key=fb_key,
                base_url=fb_url
            )

    def _call_completions(self, client: OpenAI, model: str, **kwargs) -> str:
        """Make a chat completions call and return content."""
        kwargs["model"] = model
        response = client.chat.completions.create(**kwargs)
        content = response.choices[0].message.content
        content = re.sub(r'<think>[\s\S]*?</think>', '', content).strip()
        return content

    def _is_daily_quota_error(self, error_str: str) -> bool:
        """Check if error is a daily token quota exhaustion (not a transient rate limit).
        Must match exactly 'tokens per day' or 'TPD' from Groq — NOT general 429s."""
        lower = error_str.lower()
        return 'tokens per day (tpd)' in lower or 'on tokens per day' in lower

    def _is_rate_limit_error(self, error_str: str) -> bool:
        """Check if error is any kind of rate limit."""
        return any(s in error_str.lower() for s in ['429', 'rate limit', '413', 'too large', '402', 'spend limit'])

    def _get_model_fallback_chain(self) -> list:
        """Build fallback chain: current model first, then alternates on same provider."""
        is_groq = self.base_url and 'groq.com' in self.base_url
        if not is_groq:
            return [self.model]

        chain = [self.model]
        for m in GROQ_MODEL_FALLBACK_CHAIN:
            if m != self.model:
                chain.append(m)
        return chain

    def _call_with_model_fallback(self, client: OpenAI, label: str, **kwargs) -> str:
        """
        Try the model fallback chain on the same provider.
        For each model: retry transient rate limits.
        On daily quota exhaustion: skip to next model immediately.
        """
        chain = self._get_model_fallback_chain()
        last_error = None

        for model in chain:
            for attempt in range(MAX_RETRIES):
                try:
                    result = self._call_completions(client, model, **kwargs)
                    if model != self.model:
                        logger.info("%s: using fallback model %s (primary %s exhausted)", label, model, self.model)
                    return result
                except Exception as e:
                    last_error = e
                    err_str = str(e)

                    # Daily quota exhausted → skip to next model immediately
                    if self._is_daily_quota_error(err_str):
                        logger.warning(
                            "%s: model %s daily quota exhausted, trying next model",
                            label, model
                        )
                        break  # break retry loop, try next model

                    # Transient rate limit → retry with delay
                    if self._is_rate_limit_error(err_str) and attempt < MAX_RETRIES - 1:
                        wait = RETRY_DELAY_SECONDS * (attempt + 1)
                        logger.warning(
                            "%s: %s rate limited (attempt %d/%d), waiting %ds",
                            label, model, attempt + 1, MAX_RETRIES, wait
                        )
                        time.sleep(wait)
                        continue

                    # Non-rate-limit error → raise immediately
                    raise

        # All models in chain exhausted
        raise last_error

    def chat(
        self,
        messages: List[Dict[str, str]],
        temperature: float = 0.7,
        max_tokens: int = 4096,
        response_format: Optional[Dict] = None
    ) -> str:
        """
        Send a chat request with automatic model fallback and provider fallback.

        Fallback order:
        1. Primary model on primary provider (with retry)
        2. Alternate models on primary provider (separate quotas)
        3. Fallback provider (e.g. OpenRouter)
        """
        kwargs = {
            "messages": messages,
            "temperature": temperature,
            "max_tokens": max_tokens,
        }

        if response_format:
            kwargs["response_format"] = response_format

        # Try primary provider with model fallback chain
        try:
            return self._call_with_model_fallback(self.client, "Primary", **kwargs)
        except Exception as e:
            if self.fallback_client is None:
                raise

            logger.warning(
                "All primary models exhausted (%s), switching to fallback provider: %s",
                type(e).__name__, str(e)[:200]
            )

        # Try fallback provider
        try:
            return self._call_completions(self.fallback_client, self.fallback_model, **kwargs)
        except Exception as e2:
            logger.error("Fallback provider also failed: %s", str(e2)[:200])
            raise

    def chat_json(
        self,
        messages: List[Dict[str, str]],
        temperature: float = 0.3,
        max_tokens: int = 4096
    ) -> Dict[str, Any]:
        """Send a chat request and return parsed JSON."""
        response = self.chat(
            messages=messages,
            temperature=temperature,
            max_tokens=max_tokens,
            response_format={"type": "json_object"}
        )
        cleaned_response = response.strip()
        cleaned_response = re.sub(r'^```(?:json)?\s*\n?', '', cleaned_response, flags=re.IGNORECASE)
        cleaned_response = re.sub(r'\n?```\s*$', '', cleaned_response)
        cleaned_response = cleaned_response.strip()

        try:
            return json.loads(cleaned_response)
        except json.JSONDecodeError:
            raise ValueError(f"Invalid JSON format returned by LLM: {cleaned_response}")
