"""Tests Point Class."""

__author__ = "730671130"

from lessons.CQ07.point import Point

my_point: Point = Point(3.0, 5.0)
my_point.scale_by(2.0)
my_second_point: Point = my_point.scale(2.0)

print(my_point.x)
print(my_point.y)
print(my_second_point.x)
print(my_second_point.y)