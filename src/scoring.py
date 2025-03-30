# Scoring module for the game
class Scoring:
    def __init__(self):
        self.total_score = 0

    def calculate_score(self, matches, is_successful):
        if is_successful:
            self.total_score += len(matches) * 10
        return self.total_score
