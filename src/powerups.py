# Power-ups module for the game
class PowerUps:
    def __init__(self):
        self.powerups = []

    def add_powerup(self, powerup):
        self.powerups.append(powerup)

    def get_powerups(self):
        return self.powerups
