"""Utility class for numerical operations."""

from __future__ import annotations

from typing import Union

__author__ = "730671130"


class Simpy:
    """This is a Simpy class, a single dimension implementation that is like NumPy."""
    values: list[float]

    # TODO: Your constructor and methods will go here.
    def __init__(self, values: list[float]) -> None:
        """Initializes a Simpy object."""
        self.values = values
    
    def __str__(self) -> str:
        """String magic method that returns a string in a readable form."""
        string: str = f"Simpy({self.values})"
        return string
    
    def fill(self, fill_value: float, num_values: int) -> None:
        """Fills a Simpy's values with a specific number of repeating values."""
        self.values = []
        for _ in range(0, num_values):
            self.values.append(fill_value)
    
    def arange(self, start: float, stop: float, step: float = 1.0) -> None:
        """Fills in the values attribute with a range of values from start to stop with an increment of step."""
        assert step != 0.0
        new_value: float = start
        num_steps: int = int((stop - start) / step)
        for _ in range(0, num_steps):
            self.values.append(new_value)
            new_value += step
    
    def sum(self) -> float:
        """Returns sum of all items in the values attribute."""
        the_sum = sum(self.values)
        return the_sum
    
    def __add__(self, rhs: Union[float, Simpy]) -> Simpy:
        """Operator overload with the addition operator."""
        result_values: list[float] = []
        if type(rhs).__name__ == "Simpy":
            assert len(self.values) == len(rhs.values)
            for i in range(0, len(self.values)):
                result_values.append(self.values[i] + rhs.values[i])
        else:
            for i in range(0, len(self.values)):
                result_values.append(self.values[i] + rhs)
        return Simpy(result_values)
    
    def __pow__(self, rhs: Union[float, Simpy]) -> Simpy:
        """Operator overload with the power operator."""
        result_values: list[float] = []
        if type(rhs).__name__ == "Simpy":
            assert len(self.values) == len(rhs.values)
            for i in range(0, len(self.values)):
                result_values.append(self.values[i] ** rhs.values[i])
        else:
            for i in range(0, len(self.values)):
                result_values.append(self.values[i] ** rhs)
        return Simpy(result_values)
    
    def __eq__(self, rhs: Union[float, Simpy]) -> list[bool]:
        """Returns a list of bools based on the equality of each item in values with another Simpy or float."""
        result_bools: list[bool] = []
        if type(rhs).__name__ == "Simpy":
            assert len(self.values) == len(rhs.values)
            for i in range(0, len(self.values)):
                result_bools.append(self.values[i] == rhs.values[i])
        else:
            for i in range(0, len(self.values)):
                result_bools.append(self.values[i] == rhs)
        return result_bools
    
    def __gt__(self, rhs: Union[float, Simpy]) -> list[bool]:
        """Returns a list of bools based on if an item in values is greater than a value in another Simpy or float."""
        result_bools: list[bool] = []
        if type(rhs).__name__ == "Simpy":
            assert len(self.values) == len(rhs.values)
            for i in range(0, len(self.values)):
                result_bools.append(self.values[i] > rhs.values[i])
        else:
            for i in range(0, len(self.values)):
                result_bools.append(self.values[i] > rhs)
        return result_bools
    
    def __getitem__(self, rhs: Union[int, list[bool]]) -> Union[float, Simpy]:
        """Allows subscription notation with the subscription operator used on Simpy objects."""
        if type(rhs).__name__ == "int":
            subscript: float = self.values[rhs]
        else:
            subscript: list[bool] = []
            for i in range(0, len(rhs)):
                if rhs[i] is True:
                    subscript.append(self.values[i])
        return Simpy(subscript)