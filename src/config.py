# Configuration settings for the game
class Config:
    def __init__(self):
        self.settings = {
            "volume": 0.5,
            "difficulty": "normal",
            "resolution": (800, 600)
        }

    def get_setting(self, key):
        return self.settings.get(key)

    def set_setting(self, key, value):
        self.settings[key] = value
