"""Combining two lists into a dictionary."""

__author__ = "730671130"


def zip(list_str: list[str], list_int: list[int]) -> dict[str, int]:
    """Makes dict with keys as items of the first list and values of as items of the second list."""
    new_dict: dict[str, int] = dict()
    if len(list_str) != len(list_int) or len(list_str) == 0 or len(list_int) == 0:
        return new_dict
    idx: int = 0
    while idx < len(list_str):
        new_dict[list_str[idx]] = list_int[idx]
        idx += 1
    return new_dict