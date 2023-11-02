"""Practicing with dictionary functions."""

__author__ = "730671130"


def invert(inp_dict: dict[str, str]) -> dict[str, str]:
    """This function inverts the keys and values of a dictionary."""
    new_dict: dict[str, str] = {}
    for key in inp_dict:
        for new_key in new_dict:
            if key == new_key:
                raise KeyError("There is a duplicate key.")
        new_dict[inp_dict[key]] = key
    return new_dict


def favorite_color(inp_dict: dict[str, str]) -> str:
    """This function returns the favorite color that appears most frequently."""
    fav_color: str = ""
    fav_color_count: int = 0
    color_counts: dict[str, int] = {}

    for name in inp_dict:
        if inp_dict[name] in color_counts:
            color_counts[inp_dict[name]] += 1
        else:
            color_counts[inp_dict[name]] = 1
        
        if color_counts[inp_dict[name]] > fav_color_count:
            fav_color = inp_dict[name]
            fav_color_count = color_counts[inp_dict[name]]

    return fav_color


def count(inp_list: list[str]) -> dict[str, int]:
    """This function returns a dict with each key being a unique value in the list and its values being the number of times they appear."""
    new_dict: dict[str, int] = {}
    for item in inp_list:
        if item in new_dict:
            new_dict[item] += 1
        else:
            new_dict[item] = 1
    return new_dict


def alphabetizer(inp_list: list[str]) -> dict[str, list[str]]:
    """This function makes a dict with each key being a unique letter and each value is a list of words that start with the letter."""
    new_dict: dict[str, list[str]] = {}
    for item in inp_list:
        original_item: str = item
        item = item.lower()
        if item[0] in new_dict:
            new_dict[item[0]].append(original_item)
        else:
            new_dict[item[0]] = [original_item]
    return new_dict


def update_attendance(inp_dict: dict[str, list[str]], day: str, student: str) -> dict[str, list[str]]:
    """This function updates an attendance dictionary with new info about a day a student attended."""
    if day in inp_dict:
        inp_dict[day].append(student)
    else:
        inp_dict[day] = [student]
    return inp_dict