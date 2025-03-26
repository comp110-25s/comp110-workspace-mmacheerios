__author__: str = "730572179"


def invert(my_dictionary: dict[str, str]) -> dict[str, str]:
    """inverts keys and values of a given dictionary"""
    key_list: list[str] = []
    """key list has old values"""
    for key in my_dictionary:
        key_list.append(my_dictionary[key])
    value_list: list[str] = []
    """value list has old keys"""
    for key in my_dictionary:
        value_list.append(key)
    idx: int = 0
    new_dictionary: dict[str, str] = {}
    while len(my_dictionary) > idx:
        new_dictionary[key_list[idx]] = value_list[idx]
        idx += 1
    idx = 0
    idx_1: int = 1
    while idx < len(my_dictionary):
        while idx_1 < len(my_dictionary):
            if key_list[idx] == key_list[idx_1]:
                raise KeyError("there is more than one of this key! uh-oh!")
            idx_1 += 1
        idx += 1
        idx_1 = idx + 1
    return new_dictionary


def count(the_list: list[str]) -> dict[str, int]:
    """provides number of times a value appears in a list"""
    the_dictionary: dict[str, int] = {}
    for item in the_list:
        if item in the_dictionary:
            the_dictionary[item] += 1
        else:
            the_dictionary[item] = 1
    return the_dictionary


def favorite_color(favorite_color: dict[str, str]) -> str:
    """returns the most mentioned color"""
    color_list: list[str] = []
    count_color: dict[str, int] = {}
    for key in favorite_color:
        color_list.append(key)
    for item in color_list:
        if item in count_color:
            count_color[item] += 1
        else:
            count_color[item] = 1
    highest_color: str = ""
    highest_rate: int = 0
    for key in count_color:
        if count_color[key] > highest_rate:
            highest_rate = count_color[key]
            highest_color = key
    return highest_color


def bin_len(the_list: list[str]) -> dict[int, set[str]]:
    bin_dictionary: dict[int, set[str]] = {}
    for n in the_list:
        item_length: int = len(n)
        if item_length in bin_dictionary:
            bin_dictionary[item_length].add(n)
        else:
            bin_dictionary[item_length] = {n}
    return bin_dictionary
