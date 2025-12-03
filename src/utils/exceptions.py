"""Custom exceptions for DSA Assistant"""

class DSAAssistantError(Exception):
    """Base exception for DSA Assistant"""
    pass

class APIKeyError(DSAAssistantError):
    """Raised when API keys are missing or invalid"""
    pass

class AgentExecutionError(DSAAssistantError):
    """Raised when agent execution fails"""
    pass

class CodeExecutionError(DSAAssistantError):
    """Raised when code execution fails"""
    pass

class ValidationError(DSAAssistantError):
    """Raised when data validation fails"""
    pass

class ConfigurationError(DSAAssistantError):
    """Raised when configuration is invalid"""
    pass
