"""Creating and comparing two similar methods that scale a point in a Point Class."""

from __future__ import annotations

__author__ = "730671130"


class Point:
    """This is a class to represent a point."""

    x: float
    y: float

    def __init__(self, x_init: float, y_init: float):
        """Constructor."""
        self.x = x_init
        self.y = y_init

    def scale_by(self, factor: int):
        """Scales x and y by the factor."""
        self.x = self.x * factor
        self.y = self.y * factor

    def scale(self, factor: int) -> Point:
        """Returns a new point with x and y scaled by the factor."""
        new_point: Point = Point(self.x * factor, self.y * factor)
        return new_point