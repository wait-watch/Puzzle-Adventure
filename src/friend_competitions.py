# Friend competitions module for the game
class FriendCompetitions:
    def __init__(self):
        self.competitions = []

    def add_competition(self, competition):
        self.competitions.append(competition)

    def get_competitions(self):
        return self.competitions
