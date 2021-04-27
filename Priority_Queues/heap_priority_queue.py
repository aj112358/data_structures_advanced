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

    def _swap(self, i, j):
        """Swap the elements at indices i and j of array."""
        self._data[i], self._data[j] = self._data[j], self._data[i]

    def _upheap(self, j):
        parent = self._parent(j)
        if j > 0 and self._data[j] < self._data[parent]:
            self._swap(j, parent)
            self._upheap(parent)

    def _downheap(self, j):
        if self._has_left(j):
            left = self._left(j)
            small_child = left

            if self._has_right(j):
                right = self._right(j)

                if self._data[right] < self._data[left]:  # Determine which of left and right child is smaller.
                    small_child = right
                # else:
                #     small_child = left

            if self._data[small_child] < self._data[j]:
                self._swap(j, small_child)
                self._downheap(small_child)

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
