"""Implementing a priority queue using an *unsorted* positional list.

Created By: AJ Singh
Date: April 25, 2021
"""

from Linked_Lists.positional_list import PositionalList
from priority_queue_base_class import PriorityQueueBase


class Empty(Exception):
    """The error to raise when attempting to access an element from an empty priority queue."""
    pass


class UnsortedPriorityQueue(PriorityQueueBase):
    """A minimum-oriented priority queue implemented with an unsorted positional list."""

    # Non-Public Utility Method
    def _find_min(self):
        """Returns position of item of minimal key."""
        if self.is_empty():
            raise Empty("Priority queue is empty.")

        smallest = self._data.first()
        walk = self._data.after(smallest)
        while walk is not None:
            if walk.element() < smallest.element():
                smallest = walk
            walk = self._data.after(walk)

        return smallest

    def __init__(self):
        """Create a new empty priority queue."""
        self._data = PositionalList()

    def __len__(self):
        return len(self._data)

    def add(self, key, value):
        """Add a new key-value pair to the priority queue."""
        new_item = self._Item(key, value)
        self._data.add_last(new_item)  # Since priority queue is unsorted, we just add element at the end.

    def min(self):
        pass

    def remove_min(self):
        pass
