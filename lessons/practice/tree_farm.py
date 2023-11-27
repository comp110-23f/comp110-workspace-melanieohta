"""Practice christmas tree farm class."""

from __future__ import annotations

__author__ = "730671130"


class ChristmasTreeFarm:
    """Class for a christmas tree farm."""

    plots: list[int]


    def __init__(self, plots: int, initial_planting: int) -> None:
        """Initializes a ChristmasTreeFarm object."""
        self.plots = []
        for _ in range(initial_planting):
            self.plots.append(1)
        remaining: int = plots - initial_planting
        for _ in range(remaining):
            self.plots.append(0)
    
    def plant(self, index: int) -> None:
        """Plants a tree of size 1 at the given index."""
        self.plots[index] = 1

    def growth(self) -> None:
        """Grows every planted tree by 1."""
        for i in range(len(self.plots)):
            if self.plots[i] != 0:
                self.plots[i] += 1
    
    def harvest(self, replant: bool) -> int:
        """Harvests trees of size 5 or greater and replants them if indicated."""
        harvested: int = 0
        for i in range(len(self.plots)):
            if self.plots[i] >= 5:
                harvested += 1
                self.plots[i] = 0
                if replant:
                    self.plots[i] = 1
        return harvested
    
    def __add__(self, farm: ChristmasTreeFarm) -> ChristmasTreeFarm:
        """Overloads the addition operator between 2 ChristmasTreeFarm objects."""
        trees: int = 0
        for plot in self.plots:
            if plot > 0:
                trees += 1
        for plot in farm.plots:
            if plot > 0:
                trees += 1
        return ChristmasTreeFarm(len(self.plots) + len(farm.plots), trees)