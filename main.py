# import patch_sqlite 
import streamlit as st
from src.core.app import DSAAssistantApp
from config.settings import PAGE_TITLE, PAGE_LAYOUT, SIDEBAR_STATE
from src.utils.error_handler import handle_errors
import logging

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

@handle_errors
def main():
    """Main application entry point"""
    try:
        st.set_page_config(
            page_title=PAGE_TITLE,
            layout=PAGE_LAYOUT,
            initial_sidebar_state=SIDEBAR_STATE,
            page_icon="assets/logo.svg"
        )
        
        # Initialize and run the application
        app = DSAAssistantApp()
        app.run()
    except Exception as e:
        logger.error(f"Application startup failed: {str(e)}", exc_info=True)
        st.error("❌ Failed to start the application. Please check your configuration.")
        st.exception(e)

if __name__ == "__main__":
    main()