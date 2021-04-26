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
        pass

    def min(self):
        pass

    def remove_min(self):
        pass
