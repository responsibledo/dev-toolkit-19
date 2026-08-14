from typing import Dict, Any

class Config:
    """
    A class to handle configuration settings for the application.
    """

    def __init__(self, settings: Dict[str, Any]) -> None:
        """
        Initialize the Config with a dictionary of settings.
        
        :param settings: A dictionary containing configuration settings.
        """
        self.settings = settings

    def get(self, key: str, default: Any = None) -> Any:
        """
        Retrieve a setting by its key.
        
        :param key: The key of the setting to retrieve.
        :param default: The default value to return if the key is not found.
        :return: The value of the setting or the default value.
        """
        return self.settings.get(key, default)

    def set(self, key: str, value: Any) -> None:
        """
        Set a configuration setting.
        
        :param key: The key of the setting to set.
        :param value: The value to assign to the setting.
        """
        self.settings[key] = value

    def __repr__(self) -> str:
        """
        Return a string representation of the configuration settings.
        """
        return f"Config(settings={self.settings})"