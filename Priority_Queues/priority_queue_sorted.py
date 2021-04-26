"""Implementing a sorted priority queue using a positional list.

Created By: AJ Singh
Date: April 25, 2021
"""

from priority_queue_base_class import PriorityQueueBase
from Linked_Lists.positional_list import PositionalList


class SortedPriorityQueue(PriorityQueueBase):
    """A minimum-oriented priority queue implementation with a sorted positional list."""

    def __init__(self):
        """Create a new empty priority queue."""
        self._data = PositionalList()

    def __len__(self):
        """Return number of elements in priority queue."""
        return len(self._data)

    def add(self, key, value):
        """Adds a new key-value item to the priority queue."""
        newest = self._Item(key, value)
        walk = self._data.last()  # We start at the *highest* element, and walk backwards to find correct position.

        # Finding correct position to insert new element.
        while walk is not None and newest < walk.element():
            walk = self._data.before(walk)

        if walk is None:  # Newest element is smaller than existing elements.
            self._data.add_first(newest)
        else:
            self._data.add_after(walk, newest)

    def min(self):
        pass

    def remove_min(self):
        pass
