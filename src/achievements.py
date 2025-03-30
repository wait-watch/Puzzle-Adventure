# Achievements module for the game
class Achievements:
    def __init__(self):
        self.achievements = []

    def add_achievement(self, achievement):
        self.achievements.append(achievement)

    def get_achievements(self):
        return self.achievements
