"""An implementation of a heap-based priority queue, using an array as the underlying data structure.

Created By: AJ Singh
Date: April 27, 2021
"""

from priority_queue_base_class import PriorityQueueBase


class HeapPriorityQueue(PriorityQueueBase):
    """A minimum-oriented priority queue implemented with a binary heap."""

    # ----- Non-Public Utility Functions ----- #

    def _parent(self, j):
        return (j-1) // 2

    def _left(self, j):
        return 2*j+1

    def _right(self, j):
        return 2*j+2

    def _has_left(self, j):
        return self._left(j) < len(self._data)

    def _has_right(self, j):
        return self._right(j) < len(self._data)

    def _swap(self):
        pass

    def _upheap(self):
        pass

    def _downheap(self):
        pass

    # ----- Public ADT Methods ----- #

    def __init__(self):
        """Create a new empty priority queue."""
        self._data = list()

    def __len__(self):
        pass

    def add(self):
        pass

    def min(self):
        pass

    def remove_min(self):
        pass
