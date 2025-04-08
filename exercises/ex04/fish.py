__author__: str = "730572179"

"""File to define Fish class."""


class Fish:
    """defines fish."""

    age: int

    def __init__(self):
        """constructor, assigns initial parameters."""
        self.age = 0
        return None

    def one_day(self):
        """ages the fish by one day."""
        self.age += 1
        return None
