class CustomError(Exception):
    def __init__(self, message):
        self.message = message
        super().__init__(self.message)

class InvalidInputError(CustomError):
    def __init__(self, input_value):
        message = f"Invalid input: {input_value}"
        super().__init__(message)

class ConnectionError(CustomError):
    def __init__(self, url):
        message = f"Failed to connect to: {url}"
        super().__init__(message)

class TimeoutError(CustomError):
    def __init__(self, operation):
        message = f"Operation timed out: {operation}"
        super().__init__(message)

class NotFoundError(CustomError):
    def __init__(self, resource):
        message = f"Resource not found: {resource}"
        super().__init__(message)

class PermissionDeniedError(CustomError):
    def __init__(self):
        message = "Permission denied"
        super().__init__(message)