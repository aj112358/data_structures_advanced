"""Implementing a sorted priority queue using a positional list.

Created By: AJ Singh
Date: April 25, 2021
"""

from priority_queue_base_class import PriorityQueueBase
from Linked_Lists.positional_list import PositionalList


class Empty(Exception):
    """The error to raise when attempting to access an element from an empty priority queue."""
    pass


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
        """Return, but do not remove, (k,v) tuple with a minimum key."""
        if self.is_empty():
            raise Empty("No elements in priority queue!")

        min_pos = self._data.first()  # Because our positional list is sorted!
        min_item = min_pos.element()
        return min_item._key, min_item._value

    def remove_min(self):
        """Remove and return the (k,v) tuple with a minimum key."""
        if self.is_empty():
            raise Empty("No elements in priority queue!")

        min_pos = self._data.first()  # Because our positional list is sorted!
        min_item = self._data.delete(min_pos)
        return min_item._key, min_item._value
