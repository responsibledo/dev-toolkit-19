class RobloxError(Exception):
    """Custom exception for Roblox-related errors."""
    def __init__(self, message, *args):
        super().__init__(message, *args)
        self.message = message

class NotFoundError(RobloxError):
    """Exception raised when a resource is not found."""
    def __init__(self, resource):
        super().__init__(f'{resource} not found.')
        self.resource = resource

class PermissionDeniedError(RobloxError):
    """Exception raised for permission violations."""
    def __init__(self, action):
        super().__init__(f'Permission denied for action: {action}')
        self.action = action

class InvalidDataError(RobloxError):
    """Exception raised for invalid data errors."""
    def __init__(self, data):
        super().__init__(f'Invalid data provided: {data}')
        self.data = data

class RateLimitError(RobloxError):
    """Exception raised when the rate limit is exceeded."""
    def __init__(self, retry_after):
        super().__init__(f'Rate limit exceeded. Try again after {retry_after} seconds.')
        self.retry_after = retry_after
