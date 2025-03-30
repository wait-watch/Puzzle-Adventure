import pygame
import sys
from ui import UI
from game_logic import Game
from levels import LevelManager
from rhythm import Rhythm
from scoring import Scoring
from match3 import Match3

# Initialize Pygame
pygame.init()

# Set up display
WIDTH, HEIGHT = 800, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Puzzle Pulse: Rhythm & Tiles")

# Game and UI setup
game = Game()  # Initialize the game instance
ui = UI(screen)  # Initialize UI with the screen
level_manager = LevelManager()  # Initialize level manager
match3 = Match3(game.grid)  # Initialize Match3 with the game grid
rhythm = Rhythm()  # Initialize Rhythm for beat detection
scoring = Scoring()  # Initialize Scoring for score management

def main():
    current_level = level_manager.get_level(game.level)
    ui.draw_home_screen()

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == pygame.MOUSEBUTTONDOWN:
                if ui.play_button.is_clicked(event.pos):
                    print("Starting the game...")
                    game.initialize_grid(current_level.grid_size)
                    play_game()
                elif ui.settings_button.is_clicked(event.pos):
                    print("Settings are not implemented yet.")
                elif ui.quit_button.is_clicked(event.pos):
                    pygame.quit()
                    sys.exit()

def play_game():
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == pygame.MOUSEBUTTONDOWN:
                if rhythm.detect_beat():
                    matches = match3.check_matches()
                    if matches:
                        points = scoring.calculate_score(matches, True)
                        match3.remove_matches(matches)
                        print(f"Score: {points}")
                else:
                    print("Off-beat match!")

        ui.draw_game_screen(game.grid, scoring.total_score)
        pygame.display.flip()

if __name__ == "__main__":
    main()
