from typing import Dict, Tuple

# Error messages
ERROR_MESSAGES: Dict[str, str] = {
    'invalid_input': 'Input value is not valid.',
    'not_found': 'The requested item was not found.',
    'timeout': 'The operation has timed out.',
}

# Status codes
STATUS_CODES: Dict[str, int] = {
    'success': 200,
    'not_found': 404,
    'internal_error': 500,
}

# Configuration settings as constants
class Config:
    TIMEOUT: int = 30  # seconds
    RETRY_LIMIT: int = 5
    BASE_URL: str = 'https://api.example.com/'

def get_error_message(key: str) -> str:
    """Retrieve an error message by its key.

    Args:
        key (str): The key corresponding to the error message.

    Returns:
        str: The corresponding error message or a default message if key is not found.
    """
    return ERROR_MESSAGES.get(key, 'Unknown error occurred.')

def get_status_code(key: str) -> int:
    """Retrieve a status code by its key.

    Args:
        key (str): The key corresponding to the status code.

    Returns:
        int: The corresponding status code or 500 if key is not found.
    """
    return STATUS_CODES.get(key, 500)