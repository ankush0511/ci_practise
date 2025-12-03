"""Error handling utilities"""
import streamlit as st
import logging
from functools import wraps
from typing import Callable, Any
from .exceptions import DSAAssistantError, APIKeyError, AgentExecutionError

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

def handle_errors(func: Callable) -> Callable:
    """Decorator for handling errors in functions"""
    @wraps(func)
    def wrapper(*args, **kwargs) -> Any:
        try:
            return func(*args, **kwargs)
        except APIKeyError as e:
            logger.error(f"API Key Error: {str(e)}")
            st.error(f"🔑 API Configuration Error: {str(e)}")
            st.info("Please check your .env file or Streamlit secrets configuration.")
            return None
        except AgentExecutionError as e:
            logger.error(f"Agent Execution Error: {str(e)}")
            st.error(f"🤖 Agent Error: {str(e)}")
            st.info("The AI agent encountered an issue. Please try again.")
            return None
        except Exception as e:
            logger.error(f"Unexpected error in {func.__name__}: {str(e)}", exc_info=True)
            st.error(f"❌ An unexpected error occurred: {str(e)}")
            st.info("Please try again or contact support if the issue persists.")
            return None
    return wrapper

def validate_api_keys(groq_key: str = None, google_key: str = None) -> bool:
    """Validate API keys are present"""
    if not groq_key:
        raise APIKeyError("GROQ_API_KEY is missing")
    if not google_key:
        raise APIKeyError("GOOGLE_API_KEY is missing")
    return True

def safe_agent_run(agent, query, error_message: str = "Agent execution failed"):
    """Safely run an agent with error handling"""
    try:
        result = agent.run(query)
        if not result or not hasattr(result, 'content'):
            raise AgentExecutionError(f"{error_message}: Invalid response")
        return result
    except Exception as e:
        logger.error(f"Agent run failed: {str(e)}")
        raise AgentExecutionError(f"{error_message}: {str(e)}")
