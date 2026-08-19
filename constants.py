class RobloxConstants:
    BASE_URL = 'https://www.roblox.com'
    GAME_PATH = '/games'
    USER_PATH = '/users'
    ASSET_PATH = '/asset'
    API_VERSION = 'v1'
    HEADER_CONTENT_TYPE = 'application/json'
    HEADER_USER_AGENT = 'Mozilla/5.0'

class RobloxErrorCodes:
    SUCCESS = 200
    NOT_FOUND = 404
    FORBIDDEN = 403
    SERVER_ERROR = 500

class RobloxUserRoles:
    ADMIN = 'Admin'
    MODERATOR = 'Moderator'
    PLAYER = 'Player'
    GUEST = 'Guest'

class RobloxEvents:
    USER_JOINED = 'UserJoined'
    USER_LEFT = 'UserLeft'
    GAME_STARTED = 'GameStarted'
    GAME_ENDED = 'GameEnded'

