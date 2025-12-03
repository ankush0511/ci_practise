import streamlit as st
import os
from dotenv import load_dotenv
import logging

load_dotenv()
logger = logging.getLogger(__name__)

# API Configuration with fallback
try:
    groq_api_key = st.secrets.get('GROQ_API_KEY') or os.getenv("GROQ_API_KEY")
    google_api_key = st.secrets.get('GOOGLE_API_KEY') or os.getenv("GOOGLE_API_KEY")
    
    if not groq_api_key or not google_api_key:
        logger.warning("API keys not found in secrets or environment")
except Exception as e:
    logger.error(f"Error loading API keys: {str(e)}")
    groq_api_key = os.getenv("GROQ_API_KEY")
    google_api_key = os.getenv("GOOGLE_API_KEY")

# Model Configuration
GROQ_MODEL = "llama-3.3-70b-versatile"
GEMINI_MODEL = "gemini-2.0-flash"

# UI Configuration
PAGE_TITLE = "DSA Assistant"
PAGE_LAYOUT = "wide"
SIDEBAR_STATE = "expanded"

# Application Settings
DEBUG = os.getenv("DEBUG", "False").lower() == "true"
LOG_LEVEL = os.getenv("LOG_LEVEL", "INFO")

# Timeout settings
AGENT_TIMEOUT = int(os.getenv("AGENT_TIMEOUT", "60"))
MAX_RETRIES = int(os.getenv("MAX_RETRIES", "3"))