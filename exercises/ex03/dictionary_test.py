__author__: str = "730572179"

from exercises.ex03.dictionary import invert
import pytest
from exercises.ex03.dictionary import count


test_dictionary: dict[str, str] = {"a": "z", "b": "y", "c": "x"}
return_test_dictionary: dict[str, str] = {"z": "a", "y": "b", "x": "c"}


def test_invert_use_1() -> None:
    """one use case test for invert"""
    assert invert(test_dictionary) == return_test_dictionary


def test_invert_edge() -> None:
    """edge case for invert"""
    with pytest.raises(KeyError):
        my_dictionary = {"apple": "pie", "cherry": "pie"}
        invert(my_dictionary)


test_dictionary_1: dict[str, str] = {"mess": "you", "fine": "okay"}
return_test_dictionary_1: dict[str, str] = {"you": "mess", "okay": "fine"}


def test_invert_use_2() -> None:
    """second use case test for invert"""
    assert invert(test_dictionary_1) == return_test_dictionary_1


test_count_list_0: list[str] = ["blue", "red", "blue"]
test_count_dict_0: dict[str, int] = {"blue": "2", "red": "1"}


def test_count_use_0() -> None:
    """one use case test for count"""
    assert count(test_count_list_0) == test_count_dict_0


test_count_list_1: list[str] = ["green", "red", "blue"]
test_count_dict_1: dict[str, int] = {"green": "1", "red": "1", "blue": "1"}


def test_count_use_1() -> None:
    """second use case test for count"""
    assert count(test_count_list_1) == test_count_dict_1


test_list_2: list[str] = [
    "greeen",
    "red",
    "blue",
    "green",
    "red",
    "green",
    "yellow",
    "green",
]
test_count_dict_2: dict[str, int] = {
    "greeen": "1",
    "red": "2",
    "green": "3",
    "blue": "1",
    "yellow": "1",
}


def test_count_edge_0() -> None:
    """one edge case test for count"""
    assert count(test_list_2) == test_count_dict_2


from exercises.ex03.dictionary import favorite_color

test_dict_0: dict[str, str] = {"jack": "red", "jill": "green", "eric": "red"}


def test_favorite_color_use_case_0() -> None:
    """one use case for favorite_color"""
    assert favorite_color(test_dict_0) == "red"


test_dict_1: dict[str, str] = {"jack": "red", "jill": "blue", "eric": "green"}


def test_favorite_color_use_case_1() -> None:
    """another use case for favorite_color"""
    assert favorite_color(test_dict_1) == "red"


test_dict_2: dict[str, str] = {
    "eric": "blue",
    "jill": "red",
    "jack": "green",
    "jack": "green",
    "jack": "green",
}


def test_favorite_color_edge_case_0() -> None:
    """an edge case for favorite_color"""
    assert favorite_color(test_dict_2) == "green"


from exercises.ex03.dictionary import bin_len


def test_bin_len_use_case_0() -> None:
    """a use case test of bin_len"""
    assert bin_len(["the", "quick", "fox"]) == {3: {"the", "fox"}, 5: {"quick"}}


def test_bin_len_use_case_1() -> None:
    """another use case for bin_len"""
    assert bin_len(["food", "use", "only"]) == {4: {"food", "only"}, 3: {"use"}}


def test_bin_len_edge_case_0() -> None:
    """an edge case test for bin_len"""
    assert bin_len(["", "fire", ""]) == {0: {"", ""}, 4: {"fire"}}
