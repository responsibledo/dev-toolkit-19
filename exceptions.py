class RobloxError(Exception):
    """Base class for Roblox exceptions."""
    pass

class AssetNotFoundError(RobloxError):
    """Exception raised when an asset is not found."""
    def __init__(self, asset_id):
        self.asset_id = asset_id
        super().__init__(f'Asset with ID {asset_id} not found')

class InvalidUserError(RobloxError):
    """Exception raised for invalid user actions."""
    def __init__(self, username):
        self.username = username
        super().__init__(f'Invalid user: {username}')

class PermissionDeniedError(RobloxError):
    """Exception raised when permissions are insufficient."""
    def __init__(self, action):
        self.action = action
        super().__init__(f'Permission denied for action: {action}')

class OperationTimeoutError(RobloxError):
    """Exception raised on operation timeout."""
    def __init__(self, operation):
        self.operation = operation
        super().__init__(f'Operation {operation} timed out')

# Example of raising an exception
if __name__ == '__main__':
    raise AssetNotFoundError(123456789)
