"""File to define Fish class."""


class Fish:
    """The Fish class."""

    age: int

    def __init__(self):
        """Initializes a new Fish."""
        self.age = 0
        return None
    
    def one_day(self):
        """After a day, the age of a fish increases by 1."""
        self.age += 1
        return None