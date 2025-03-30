# Levels module for the game
class LevelManager:
    def __init__(self):
        self.levels = []

    def add_level(self, level):
        self.levels.append(level)

    def get_level(self, level_number):
        return self.levels[level_number]
