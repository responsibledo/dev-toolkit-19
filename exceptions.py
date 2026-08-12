class CustomError(Exception):
    def __init__(self, message, code=None):
        super().__init__(message)
        self.code = code

class ValidationError(CustomError):
    def __init__(self, field, message):
        super().__init__(f'Validation error on {field}: {message}')
        self.field = field

class NotFoundError(CustomError):
    def __init__(self, resource):
        super().__init__(f'Resource not found: {resource}')
        self.resource = resource

class DatabaseError(CustomError):
    def __init__(self, message, db_code):
        super().__init__(message)
        self.db_code = db_code

class PermissionError(CustomError):
    def __init__(self, action):
        super().__init__(f'Permission denied for action: {action}')
        self.action = action
