"""Node Class."""

from __future__ import annotations


class Node:
    """My Node class for linked lists."""
    
    data: int
    next: Node | None
    
    def __init__(self, data: int, next: Node | None):
        """Construct Node."""
        self.data = data
        self. next = next
    
    def pretty_list(self) -> str:
        if self.next == None:
            # base case, where recursion ends
            return str(self.data)
        else:
            # recursive step
            return str(self.data) + " -> " + self.next.pretty_list()

    def __str__(self) -> str:
        """Produce a string visualization of the linked list."""
        if self.next is None:
            # base case (where it ends!)
            return f"{self.data} -> None"
        else:
            return f"{self.data} -> {self.next}"
        
    def head(self):
        return None
    
    def tail(self):
        return None
    
    def last(self):
        return None