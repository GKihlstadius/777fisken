"""
Configuration management
Loads configuration from the project root .env file
"""

import os
from dotenv import load_dotenv

# Load .env file from project root
# Path: MiroFish/.env (relative to backend/app/config.py)
project_root_env = os.path.join(os.path.dirname(__file__), '../../.env')

if os.path.exists(project_root_env):
    load_dotenv(project_root_env, override=True)
else:
    # If no .env in root, try loading environment variables (for production)
    load_dotenv(override=True)


class Config:
    """Flask configuration class"""

    # Flask configuration
    SECRET_KEY = os.environ.get('SECRET_KEY', 'mirofish-secret-key')
    DEBUG = os.environ.get('FLASK_DEBUG', 'True').lower() == 'true'

    # JSON configuration - disable ASCII escaping for proper Unicode display
    JSON_AS_ASCII = False

    # Primary LLM configuration (Groq)
    PRIMARY_LLM_API_KEY = os.environ.get('PRIMARY_LLM_API_KEY')
    PRIMARY_LLM_BASE_URL = os.environ.get('PRIMARY_LLM_BASE_URL', 'https://api.groq.com/openai/v1')
    PRIMARY_LLM_MODEL = os.environ.get('PRIMARY_LLM_MODEL', 'llama-3.3-70b-versatile')

    # Fallback LLM configuration (OpenRouter)
    FALLBACK_LLM_API_KEY = os.environ.get('FALLBACK_LLM_API_KEY')
    FALLBACK_LLM_BASE_URL = os.environ.get('FALLBACK_LLM_BASE_URL', 'https://openrouter.ai/api/v1')
    FALLBACK_LLM_MODEL = os.environ.get('FALLBACK_LLM_MODEL', 'meta-llama/llama-3.3-70b-instruct:free')

    # Report LLM configuration (separate model for report generation to avoid quota conflicts)
    REPORT_LLM_API_KEY = os.environ.get('REPORT_LLM_API_KEY')
    REPORT_LLM_BASE_URL = os.environ.get('REPORT_LLM_BASE_URL')
    REPORT_LLM_MODEL = os.environ.get('REPORT_LLM_MODEL')

    # Legacy LLM configuration (backwards compatible)
    LLM_API_KEY = os.environ.get('LLM_API_KEY')
    LLM_BASE_URL = os.environ.get('LLM_BASE_URL', 'https://api.openai.com/v1')
    LLM_MODEL_NAME = os.environ.get('LLM_MODEL_NAME', 'gpt-4o-mini')

    # Zep configuration
    ZEP_API_KEY = os.environ.get('ZEP_API_KEY')

    # File upload configuration
    MAX_CONTENT_LENGTH = 50 * 1024 * 1024  # 50MB
    UPLOAD_FOLDER = os.path.join(os.path.dirname(__file__), '../uploads')
    ALLOWED_EXTENSIONS = {'pdf', 'md', 'txt', 'markdown'}

    # Text processing configuration
    DEFAULT_CHUNK_SIZE = 500
    DEFAULT_CHUNK_OVERLAP = 50

    # OASIS simulation configuration
    OASIS_DEFAULT_MAX_ROUNDS = int(os.environ.get('OASIS_DEFAULT_MAX_ROUNDS', '10'))
    OASIS_SIMULATION_DATA_DIR = os.path.join(os.path.dirname(__file__), '../uploads/simulations')

    # OASIS platform available actions
    OASIS_TWITTER_ACTIONS = [
        'CREATE_POST', 'LIKE_POST', 'REPOST', 'FOLLOW', 'DO_NOTHING', 'QUOTE_POST'
    ]
    OASIS_REDDIT_ACTIONS = [
        'LIKE_POST', 'DISLIKE_POST', 'CREATE_POST', 'CREATE_COMMENT',
        'LIKE_COMMENT', 'DISLIKE_COMMENT', 'SEARCH_POSTS', 'SEARCH_USER',
        'TREND', 'REFRESH', 'DO_NOTHING', 'FOLLOW', 'MUTE'
    ]

    # Report Agent configuration
    REPORT_AGENT_MAX_TOOL_CALLS = int(os.environ.get('REPORT_AGENT_MAX_TOOL_CALLS', '5'))
    REPORT_AGENT_MAX_REFLECTION_ROUNDS = int(os.environ.get('REPORT_AGENT_MAX_REFLECTION_ROUNDS', '2'))
    REPORT_AGENT_TEMPERATURE = float(os.environ.get('REPORT_AGENT_TEMPERATURE', '0.5'))

    @classmethod
    def get_effective_llm_config(cls):
        """Get the effective LLM configuration, preferring PRIMARY > LEGACY"""
        if cls.PRIMARY_LLM_API_KEY:
            return cls.PRIMARY_LLM_API_KEY, cls.PRIMARY_LLM_BASE_URL, cls.PRIMARY_LLM_MODEL
        if cls.LLM_API_KEY:
            return cls.LLM_API_KEY, cls.LLM_BASE_URL, cls.LLM_MODEL_NAME
        return None, cls.PRIMARY_LLM_BASE_URL, cls.PRIMARY_LLM_MODEL

    @classmethod
    def get_fallback_llm_config(cls):
        """Get the fallback LLM configuration"""
        if cls.FALLBACK_LLM_API_KEY:
            return cls.FALLBACK_LLM_API_KEY, cls.FALLBACK_LLM_BASE_URL, cls.FALLBACK_LLM_MODEL
        return None, None, None

    @classmethod
    def get_report_llm_config(cls):
        """Get report-specific LLM config, falls back to primary if not set"""
        if cls.REPORT_LLM_API_KEY:
            return cls.REPORT_LLM_API_KEY, cls.REPORT_LLM_BASE_URL, cls.REPORT_LLM_MODEL
        return cls.get_effective_llm_config()

    @classmethod
    def validate(cls):
        """Validate required configuration"""
        errors = []
        api_key, _, _ = cls.get_effective_llm_config()
        if not api_key:
            errors.append("LLM API key not configured (set PRIMARY_LLM_API_KEY or LLM_API_KEY)")
        if not cls.ZEP_API_KEY:
            errors.append("ZEP_API_KEY not configured")
        return errors
