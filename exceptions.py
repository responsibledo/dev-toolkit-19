class ValidationError(Exception):
    """Exception raised for validation errors."""

    def __init__(self, message, field):
        self.message = message
        self.field = field
        super().__init__(self.message)

    def __str__(self):
        return f'{self.field}: {self.message}'

class DatabaseError(Exception):
    """Exception raised for database connection errors."""

    def __init__(self, message):
        self.message = message
        super().__init__(self.message)

    def __str__(self):
        return f'Database error: {self.message}'

class AuthenticationError(Exception):
    """Exception raised for authentication failures."""

    def __init__(self, username):
        self.username = username
        self.message = f'Authentication failed for user: {username}'
        super().__init__(self.message)

    def __str__(self):
        return self.message

class PermissionError(Exception):
    """Exception raised for permission related errors."""

    def __init__(self, operation):
        self.operation = operation
        self.message = f'Permission denied for operation: {operation}'
        super().__init__(self.message)

    def __str__(self):
        return self.message
