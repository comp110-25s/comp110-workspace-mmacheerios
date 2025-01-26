"""Calculates number of items and cost of a tea party depending on number of guests"""

__author__: str = "730572179"


def main_planner(guests: int):
    """entrypoint of the tea party planning program"""
    print("A Cozy Tea Party for " + str(guests) + " People!")
    print("Tea Bags: " + str(tea_bags(people=guests)))
    print("Treats: " + str(treats(people=guests)))
    print(
        "Cost: $"
        + str(
            cost(tea_count=tea_bags(people=guests), treat_count=treats(people=guests))
        )
    )
    return None


def tea_bags(people: int) -> int:
    """computes number of tea bags per guest"""
    return 2 * people


def treats(people: int) -> int:
    """computes number of treats per guest"""
    return int(tea_bags(people=people) * 1.5)


def cost(tea_count: int, treat_count: int) -> float:
    """computes cost of having guests at tea party"""
    return 0.50 * tea_count + 0.75 * treat_count


if __name__ == "__main__":
    main_planner(guests=int(input("How many guests are attending your tea party?")))
