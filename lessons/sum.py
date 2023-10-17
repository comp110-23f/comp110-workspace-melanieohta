"""Summing the elements of a list using different loops."""

__author__ = "730671130"


def w_sum(vals: list[float]) -> float:
    """Returns sum of list of floats using while loop."""
    i: int = 0
    sum: float = 0.0
    while i < len(vals):
        sum += vals[i]
        i += 1
    return sum


def f_sum(vals: list[float]) -> float:
    """Returns sum of list of floats using a for loop but not range."""
    sum: float = 0.0
    for i in vals:
        sum += i
    return sum


def f_range_sum(vals: list[float]) -> float:
    """Returns sum of list of floats using a for loop with range."""
    sum: float = 0.0
    for i in range(0, len(vals)):
        sum += vals[i]
    return sum