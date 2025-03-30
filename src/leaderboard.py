# Leaderboard module for the game
class Leaderboard:
    def __init__(self):
        self.scores = {}

    def add_score(self, player, score):
        self.scores[player] = score

    def get_scores(self):
        return self.scores
