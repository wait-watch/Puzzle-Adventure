# Game logic module for the game
class Game:
    def __init__(self):
        self.level = 1
        self.grid = []

    def initialize_grid(self, size):
        self.grid = [[0] * size for _ in range(size)]
