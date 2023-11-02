"""Practicing with dictionary functions."""

__author__ = "730671130"


def invert(dict: dict[str, str]) -> dict[str, str]:
    """This function inverts the keys and values of a dictionary."""
    new_dict: dict[str, str] = dict()
    for key in dict:
        for new_key in new_dict:
            if key == new_key:
                raise KeyError("There is a duplicate key.")
        new_dict[dict[key]] = key
    return new_dict


def favorite_color(dict: dict[str, str]) -> str:
    """This function returns the favorite color that appears most frequently."""
    fav_color: str = ""
    fav_color_count: int = 0
    color_counts: dict[str, int] = {}

    for name in dict:
        if dict[name] in color_counts:
            color_counts[dict[name]] += 1
        else:
            color_counts[dict[name]] = 1
        
        if color_counts[dict[name]] > fav_color_count:
            fav_color = dict[name]
            fav_color_count = color_counts[dict[name]]

    return fav_color


def count(list: list[str]) -> dict[str, int]:
    """This function returns a dict with each key being a unique value in the list and its values being the number of times they appear."""
    new_dict: dict[str, int] = {}
    for item in list:
        if item in new_dict:
            new_dict[item] += 1
        else:
            new_dict[item] = 1
    return new_dict


def alphabetizer(list: list[str]) -> dict[str, list[str]]:
    """This function makes a dict with each key being a unique letter and each value is a list of words that start with the letter."""
    new_dict: dict[str, list[str]] = {}
    for item in list:
        if item[0] in new_dict:
            new_dict[item[0]] += item
        else:
            new_dict[item[0]] = item
    return new_dict


def update_attendance(dict: dict[str, list[str]], day: str, student: str) -> dict[str, list[str]]:
    """This function updates an attendance dictionary with new info about a day a student attended."""
    if day in dict:
        dict[day] += student
    else:
        dict[day] = student
    return dict