"""Odd and Even Practice Function."""

__author__ = "730671130"


def odd_and_even(list: list[int]) -> list[int]:
    """Creates new list with the odd numbers with even indexes of a list."""
    new_list: list[int] = []
    i: int = 0
    for num in list:
        if num % 2 == 1 and i % 2 == 0:
            new_list.append(num)
        i += 1
    return new_list