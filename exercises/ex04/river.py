"""File to define River class."""

from exercises.ex04.fish import Fish
from exercises.ex04.bear import Bear


class River:
    day: int
    """what day of the river's lifecycle you are modeling"""
    bears: list  # type: ignore
    """each object in list is bear in the river"""
    fish: list  # type: ignore
    """each object in list is a fish in the river"""

    def __init__(self, num_fish: int, num_bears: int):
        """New River with num_fish Fish and num_bears Bears"""
        self.day: int = 0
        self.fish: list[Fish] = []
        self.bears: list[Bear] = []
        # populate the river with fish and bears
        for _ in range(0, num_fish):
            self.fish.append(Fish())
        for _ in range(0, num_bears):
            self.bears.append(Bear())

    def check_ages(self):
        ages_fish: list[Fish] = []
        for item in self.fish:
            if item.age <= 3:
                ages_fish.append(item)
        ages_bears: list[Bear] = []
        self.fish = ages_fish
        self.bears = ages_bears
        for item in self.bears:
            if item.age <= 5:
                ages_bears.append(item)
        return None

    def remove_fish(self, amount: int) -> None:
        idx: int = 0
        while idx < amount:
            self.fish.pop(0)
            idx += 1
        return None

    def bears_eating(self):
        if len(self.fish) > 5:
            self.remove_fish(3)
            Bear.eat(3)  # type: ignore
        return None

    def check_hunger(self):
        surviving_bears: list = []
        for item in self.bears:
            if item.hunger_score < 0:
                surviving_bears.append(item)
        self.bears = surviving_bears
        return None

    def repopulate_fish(self):
        number: int = (len(self.fish) // 2) * 4
        idx: int = 0
        while idx < number:
            self.fish.append(Fish())
        return None

    def repopulate_bears(self):
        number: int = len(self.bears) // 2
        idx: int = 0
        while idx < number:
            self.bears.append(Bear())
            idx += 1
        return None

    def view_river(self):
        print(
            f"~~~ Day {self.day}: ~~~ Fish population: {len(self.fish)} Bear population: {len(self.bears)}"
        )
        return None

    def one_river_day(self):
        """Simulate one day of life in the river"""
        # Increase day by 1
        self.day += 1
        # Simulate one day for all Bears
        for bear in self.bears:
            bear.one_day()
        # Simulate one day for all Fish
        for fish in self.fish:
            fish.one_day()
        # Simulate Bear's eating
        self.bears_eating()
        # Remove hungry Bear's from River
        self.check_hunger()
        # Remove old Fish and Bear's from River
        self.check_ages()
        # Simulate Fish repopulation
        self.repopulate_fish()
        # Simulate Bear repopulation
        self.repopulate_bears()
        # Visualize River
        self.view_river()

    def one_river_week(self) -> None:
        idx: int = 1
        while idx <= 7:
            self.one_river_day()
            idx += 1
