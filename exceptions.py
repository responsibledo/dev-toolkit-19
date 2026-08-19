class RobloxError(Exception):
    pass

class ResourceNotFound(RobloxError):
    def __init__(self, resource_id):
        super().__init__(f'Resource with ID {resource_id} not found.')
        self.resource_id = resource_id

class InvalidInput(RobloxError):
    def __init__(self, input_value):
        super().__init__(f'Invalid input: {input_value}')
        self.input_value = input_value

class PermissionDenied(RobloxError):
    def __init__(self, action):
        super().__init__(f'Permission denied for action: {action}')
        self.action = action

class ActionTimeout(RobloxError):
    def __init__(self, action, timeout):
        super().__init__(f'Action {action} timed out after {timeout} seconds.')
        self.action = action
        self.timeout = timeout

def handle_exceptions(func):
    def wrapper(*args, **kwargs):
        try:
            return func(*args, **kwargs)
        except RobloxError as e:
            print(f'Error: {e}')
    return wrapper
