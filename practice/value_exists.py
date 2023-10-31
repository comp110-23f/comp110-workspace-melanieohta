"""Value exists practice function."""

__author__ = "730671130"


def value_exists(dict: dict[str, int], num: int) -> bool:
    """Returns True if a value exists inside of a dictionary, and False otherwise."""
    for key in dict:
        if dict[key] == num:
            return True
    return False