"""File to define Bear class."""


class Bear:
    """The Bear class."""

    age: int
    hunger_score: int

    def __init__(self):
        """Initializes a new Bear."""
        self.age = 0
        self.hunger_score = 0
        return None
    
    def one_day(self):
        """After a day, the age of a bear increases by 1 and hunger_score decreases by 1."""
        self.age += 1
        self.hunger_score -= 1
        return None
    
    def eat(self, num_fish: int):
        """A bear's hunger_score increases by the number of fish they eat."""
        self.hunger_score += num_fish
        return None