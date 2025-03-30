class HomeScreen:
    def __init__(self):
        self.options = ["Play", "Settings", "Profile"]

    def display(self):
        print("Home Screen Options:")
        for option in self.options:
            print(f"- {option}")

# Example usage
home_screen = HomeScreen()
home_screen.display()
