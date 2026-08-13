import json
from pathlib import Path

class ConfigLoader:
    def __init__(self, default_config: str):
        self.default_config_path = Path(default_config)
        self.config = self.load_defaults()

    def load_defaults(self):
        with open(self.default_config_path, 'r') as file:
            return json.load(file)

    def load_user_config(self, user_config: str):
        user_config_path = Path(user_config)
        if user_config_path.is_file():
            with open(user_config_path, 'r') as file:
                user_config_data = json.load(file)
            self.config.update(user_config_data)
        else:
            print(f'User config {user_config} not found. Using defaults.')

    def get(self, key: str, default=None):
        return self.config.get(key, default)

if __name__ == '__main__':
    loader = ConfigLoader('default_config.json')
    loader.load_user_config('user_config.json')
    print(loader.get('some_key', 'default_value'))