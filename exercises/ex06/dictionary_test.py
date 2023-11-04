"""Unit tests for the functions in exercise 6 that test their correctness."""

__author__ = "730671130"

from exercises.ex06.dictionary import invert, favorite_color, count, alphabetizer, update_attendance

import pytest

# invert test


def test_invert_empty_dict() -> None:
    """The function call invert({}) should return {}."""
    assert invert({}) == {}


def test_invert_one_key() -> None:
    """The function call invert({"Key": "Value}) should return {"Value": "Key"}."""
    test_dict: dict[str, str] = {"Key": "Value"}
    assert invert(test_dict) == {"Value": "Key"}


def test_invert_two_keys() -> None:
    """The function call invert({"Monday": "Cloudy", "Tuesday": "Sunny"}) should return {"Cloudy": "Monday", "Sunny": "Tuesday"}."""    
    test_dict: dict[str, str] = {"Monday": "Cloudy", "Tuesday": "Sunny"}
    assert invert(test_dict) == {"Cloudy": "Monday", "Sunny": "Tuesday"}


def test_invert_error() -> None:
    """This tests a KeyError being raised in the invert function."""
    with pytest.raises(KeyError):
        my_dictionary = {'alyssa': 'byrnes', 'adam': 'byrnes'}
        invert(my_dictionary)


# favorite_color test

def test_color_empty_dict() -> None:
    """The function call favorite_color({}) should return ""."""
    assert favorite_color({}) == ""


def test_color_one_name() -> None:
    """The function call favorite_color({"Bob": "Blue"}) should return "Blue"."""
    test_dict: dict[str, str] = {"Bob": "Blue"}
    assert favorite_color(test_dict) == "Blue"


def test_color_three_names() -> None:
    """The function call favorite_color({"Bob": "Blue", "Rob": "Red", "Tim": "Red"}) should return "Red"."""
    test_dict: dict[str, str] = {"Bob": "Blue", "Rob": "Red", "Tim": "Red"}
    assert favorite_color(test_dict) == "Red"


# count test

def test_count_empty_list() -> None:
    """The function call count([]) should return {}."""
    assert count([]) == {}


def test_count_list_two_unique() -> None:
    """The function call count(["dog, "cat", "dog"]) should return {"dog": 2, "cat": 1}."""
    test_list: list[str] = ["dog", "cat", "dog"]
    assert count(test_list) == {"dog": 2, "cat": 1}


def test_count_list_three_unique() -> None:
    """The function call count(["dog, "cat", "dog", "pig", "pig"]) should return {"dog": 2, "cat": 1, "pig": 2}."""
    test_list: list[str] = ["dog", "cat", "dog", "pig", "pig"]
    assert count(test_list) == {"dog": 2, "cat": 1, "pig": 2}


# alphabetizer test

def test_alphabetizer_empty_list() -> None:
    """The function call alphabetizer([]) should return {}."""
    assert alphabetizer([]) == {}


def test_alphabetizer_list_three() -> None:
    """The function call alphabetizer(["bat", "car", "ball"]) should return {"b": ["bat", "ball"], "c": ["car"]}."""
    test_list: list[str] = ["bat", "car", "ball"]
    assert alphabetizer(test_list) == {"b": ["bat", "ball"], "c": ["car"]}


def test_alphabetizer_list_four() -> None:
    """The function call alphabetizer(["bat", "car", "ball", "horse"]) should return {"b": ["bat", "ball"], "c": ["car"], "h": ["horse"]}."""
    test_list: list[str] = ["bat", "car", "ball", "horse"]
    assert alphabetizer(test_list) == {"b": ["bat", "ball"], "c": ["car"], "h": ["horse"]}


# update_attendance test

def test_attendance_empty_dict() -> None:
    """The function call update_attendance({}) should return {}."""
    test_dict: dict[str, list[str]] = {}
    assert update_attendance(test_dict, "", "") == {"": [""]}


def test_attendance_two_days() -> None:
    """The function call update_attendance({"Monday": ["Jim"], "Tuesday": ["Pam"]}, "Monday", "Dwight") should return {"Monday": ["Jim", "Dwight"], "Tuesday": ["Pam"]}."""
    test_dict: dict[str, list[str]] = {"Monday": ["Jim"], "Tuesday": ["Pam"]}
    assert update_attendance(test_dict, "Monday", "Dwight") == {"Monday": ["Jim", "Dwight"], "Tuesday": ["Pam"]}


def test_attendance_three_days() -> None:
    """The function call update_attendance({"Monday": ["Jim", "Dwight"], "Tuesday": ["Pam"]}, "Friday", "Micheal") should return {"Monday": ["Jim", "Dwight"], "Tuesday": ["Pam"], "Friday": ["Micheal"]}."""
    test_dict: dict[str, list[str]] = {"Monday": ["Jim", "Dwight"], "Tuesday": ["Pam"]}
    assert update_attendance(test_dict, "Friday", "Micheal") == {"Monday": ["Jim", "Dwight"], "Tuesday": ["Pam"], "Friday": ["Micheal"]}