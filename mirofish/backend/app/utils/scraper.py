"""
Web scraper using Cloudflare Browser Rendering API.
Renders JavaScript-heavy pages (like Svenska Spel) and extracts content.
"""

import os
import re
import logging
import requests
from typing import Optional, Dict, Any

logger = logging.getLogger(__name__)

CF_ACCOUNT_ID = os.environ.get("CF_ACCOUNT_ID", "")
CF_API_TOKEN = os.environ.get("CF_API_TOKEN", "")
CF_RENDER_URL = f"https://api.cloudflare.com/client/v4/accounts/{CF_ACCOUNT_ID}/browser-rendering/content"


def render_page(url: str, wait_timeout: int = 8000) -> Optional[str]:
    """
    Render a JavaScript-heavy page using Cloudflare Browser Rendering API.

    Args:
        url: Page URL to render
        wait_timeout: Milliseconds to wait for JS to load (default 8s)

    Returns:
        Raw HTML string, or None on failure
    """
    token = CF_API_TOKEN
    if not token:
        logger.error("CF_API_TOKEN not set — cannot use Cloudflare Browser Rendering")
        return None

    try:
        resp = requests.post(
            CF_RENDER_URL,
            headers={
                "Authorization": f"Bearer {token}",
                "Content-Type": "application/json",
            },
            json={"url": url, "waitForTimeout": wait_timeout},
            timeout=30,
        )
        data = resp.json()
        if not data.get("success"):
            logger.error("Cloudflare render failed: %s", data.get("errors"))
            return None
        return data.get("result", "")
    except Exception as e:
        logger.error("Cloudflare render error: %s", e)
        return None


def html_to_text(html: str) -> str:
    """Strip HTML tags and return clean text lines."""
    text = re.sub(r"<script[^>]*>.*?</script>", "", html, flags=re.DOTALL)
    text = re.sub(r"<style[^>]*>.*?</style>", "", text, flags=re.DOTALL)
    text = re.sub(r"<[^>]+>", "\n", text)
    text = re.sub(r"&nbsp;", " ", text)
    text = re.sub(r"&amp;", "&", text)
    text = re.sub(r"\n\s*\n", "\n", text)
    lines = [l.strip() for l in text.split("\n") if l.strip() and len(l.strip()) > 1]
    return "\n".join(lines)


def scrape_svenskaspel_odds(url: str) -> Dict[str, Any]:
    """
    Scrape betting odds from a Svenska Spel Oddset match page.

    Args:
        url: Full Svenska Spel match URL

    Returns:
        Dict with match info and odds, e.g.:
        {
            "match": "HV 71 - Leksands IF",
            "kickoff": "Idag 18:00",
            "odds_1x2": {"home": 2.25, "draw": 4.25, "away": 2.85},
            "odds_incl_ot": {"home": 1.73, "away": 2.06},
            "over_under": {"line": 5.5, "over": 2.25, "under": 1.64},
            "handicap": {"home": {"line": -0.5, "odds": 2.20}, "away": {"line": 0.5, "odds": 1.68}},
            "raw_text": "...",
        }
    """
    html = render_page(url)
    if not html:
        return {"error": "Failed to render page"}

    text = html_to_text(html)
    lines = text.split("\n")

    result = {"url": url, "raw_lines": lines, "markets": {}}

    # Extract match title
    for line in lines:
        if " - " in line and ("IF" in line or "HV" in line or "AIK" in line):
            result["match"] = line.split("Betting")[0].strip()
            break

    # Extract kickoff
    for line in lines:
        if "Matchstart:" in line:
            result["kickoff"] = line.replace("Matchstart:", "").strip()
            break

    # Parse odds by scanning for known market headers + numeric values
    def find_odds_after(marker: str, count: int) -> list:
        """Find `count` numeric values after a line containing `marker`."""
        nums = []
        found = False
        for line in lines:
            if marker.lower() in line.lower():
                found = True
                continue
            if found:
                try:
                    val = float(line.replace(",", "."))
                    nums.append(val)
                    if len(nums) >= count:
                        return nums
                except ValueError:
                    # Skip non-numeric but keep looking
                    if len(nums) > 0 and len(line) > 20:
                        break  # Moved past the odds block
        return nums

    # 1X2
    odds_1x2 = find_odds_after("Match Odds - Ordinarie tid", 3)
    if len(odds_1x2) >= 3:
        result["markets"]["1x2"] = {
            "home": odds_1x2[0],
            "draw": odds_1x2[1],
            "away": odds_1x2[2],
        }

    # Including OT
    odds_ot = find_odds_after("Inklusive förlängning", 2)
    if len(odds_ot) >= 2:
        result["markets"]["incl_ot"] = {
            "home": odds_ot[0],
            "away": odds_ot[1],
        }

    # Over/Under
    odds_ou = find_odds_after("Totala mål", 3)
    if len(odds_ou) >= 3:
        result["markets"]["over_under"] = {
            "line": odds_ou[0],
            "over": odds_ou[1],
            "under": odds_ou[2],
        }

    # Handicap
    odds_hc = find_odds_after("Handicap", 4)
    if len(odds_hc) >= 4:
        result["markets"]["handicap"] = {
            "home_line": odds_hc[0],
            "home_odds": odds_hc[1],
            "away_line": odds_hc[2],
            "away_odds": odds_hc[3],
        }

    return result
