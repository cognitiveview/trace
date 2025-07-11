"""
Sample plugin for testing the trace SDK
"""

def hello_world(name: str = "World") -> str:
    """
    A simple hello world function for testing the SDK
    
    Args:
        name: Name to greet (default: "World")
        
    Returns:
        A greeting message
    """
    return f"Hello, {name}! This is the trace SDK."

def add_numbers(a: int, b: int) -> int:
    """
    Add two numbers together
    
    Args:
        a: First number
        b: Second number
        
    Returns:
        Sum of a and b
    """
    return a + b

def get_sdk_info() -> dict:
    """
    Get information about the SDK
    
    Returns:
        Dictionary with SDK information
    """
    return {
        "name": "trace",
        "version": "0.1.0",
        "description": "A comprehensive tracing and monitoring library for ML/AI applications",
        "providers": ["deepeval", "evidently", "opik"]
    }