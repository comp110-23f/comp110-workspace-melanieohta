"""Test my zip function."""

__author__ = "730671130"

from lessons.zip import zip


def test_empty_lists() -> None:
    """zip([], []) should return {}."""
    assert zip([], []) == {}


def test_lists_length_two() -> None:
    """zip(["Heads", "Tails"], [10, 5]) should return {'Heads': 10, 'Tails': 5}."""
    assert zip(["Heads", "Tails"], [10, 5]) == {'Heads': 10, 'Tails': 5}


def test_lists_length_three() -> None:
    """zip(["Sunday", "Monday", "Tuesday"], [10, 5]) should return {'Sunday': 1, 'Monday': 2, 'Tuesday': 3}."""
    assert zip(["Sunday", "Monday", "Tuesday"], [1, 2, 3]) == {'Sunday': 1, 'Monday': 2, 'Tuesday': 3}