"""File to define River class."""

__author__ = "730671130"

from exercises.ex08.fish import Fish
from exercises.ex08.bear import Bear


class River:
    """The River class."""

    day: int
    bears: list
    fish: list

    def __init__(self, num_fish: int, num_bears: int):
        """New River with num_fish Fish and num_bears Bears."""
        self.day: int = 0
        self.fish: list[Fish] = []
        self.bears: list[Bear] = []
        # populate the river with fish and bears
        for x in range(0, num_fish):
            self.fish.append(Fish())
        for x in range(0, num_bears):
            self.bears.append(Bear())

    def check_ages(self):
        """Checks ages of bears and fish and removes them if they are too old."""
        new_bears: list[Bear] = []
        for bear in self.bears:
            if bear.age <= 5:
                new_bears.append(bear)
        self.bears = new_bears
        new_fish: list[Fish] = []
        for fish in self.fish:
            if fish.age <= 3:
                new_fish.append(fish)
        self.fish = new_fish
        return None

    def bears_eating(self):
        """A bear will eat 3 fish if there are more than 5 fish in the river."""
        for bear in self.bears:
            if len(self.fish) >= 5:
                bear.eat(3)
                self.remove_fish(3)
        return None
    
    def check_hunger(self):
        """Checks hunger of bears and removes them if their hunger_score goes below 0."""
        new_bears: list[Bear] = []
        for bear in self.bears:
            if bear.hunger_score >= 0:
                new_bears.append(bear)
        self.bears = new_bears
        return None
        
    def repopulate_fish(self):
        """Repopulates fish in river. Every 2 fish equals 4 new fish."""
        num_new_fish = len(self.fish) // 2 * 4
        for _ in range(0, num_new_fish):
            self.fish.append(Fish())
        return None
    
    def repopulate_bears(self):
        """Repopulates bears in the river. Every 2 bears equals 1 new bear."""
        num_new_bears = len(self.bears) // 2
        for _ in range(0, num_new_bears):
            self.bears.append(Bear())
        return None
    
    def __str__(self) -> str:
        """String magic method that prints view_river in readable way."""
        r_string: str = f"~~~ Day {self.day}: ~~~ \n Fish population: {len(self.fish)} \n Bear population: {len(self.bears)}"
        return r_string

    def view_river(self):
        """Prints out a summary of the river."""
        print(self.__str__())
        return None
            
    def one_river_day(self):
        """Simulate one day of life in the river."""
        # Increase day by 1
        self.day += 1
        # Simulate one day for all Bears
        for bear in self.bears:
            bear.one_day()
        # Simulate one day for all Fish
        for fish in self.fish:
            fish.one_day()
        # Simulate Bear's eating
        self.bears_eating()
        # Remove hungry Bear's from River
        self.check_hunger()
        # Remove old Fish and Bear's from River
        self.check_ages()
        # Simulate Fish repopulation
        self.repopulate_fish()
        # Simulate Bear repopulation
        self.repopulate_bears()
        # Visualize River
        self.view_river()
    
    def one_river_week(self):
        """Runs the one_river_day function 7 times for a week."""
        for _ in range(0, 7):
            self.one_river_day()
        return None
    
    def remove_fish(self, amount: int):
        """Removes the given amount of fish from the river."""
        for _ in range(0, amount):
            self.fish.pop(0)
        return None