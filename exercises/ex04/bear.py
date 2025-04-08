__author__: str = "730572179"


"""File to define Bear class."""


class Bear:
    """defines the bear"""

    age: int
    hunger_score: int

    def __init__(self):
        """constructor, assigns initial values."""
        self.age = 0
        self.hunger_score = 0
        return None

    def one_day(self):
        """ages bear by one day."""
        self.age += 1
        self.hunger_score -= 1
        return None

    def eat(self, num_fish: int) -> None:
        """simulates bear eatinG!"""
        self.hunger_score += num_fish
        return None
