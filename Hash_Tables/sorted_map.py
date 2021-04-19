"""An implementation of a "sorted map", where the keys are sorted using the natural ordering on the keys, taken from
book.

Created By: AJ Singh
Date: April 18, 2021
"""

from hash_map_base_class import MapBase


class SortedTableMap(MapBase):
    """A map implementation using a sorted array."""

    # ----- Non-Public Utility Method ----- #
    def _find_index(self, k, low, high):
        """Return the index of the left-most item with key greater than or equal to k. Return high+1 if no such item
        exists.

        So, index j will be returned such that:
            (i) All items of slice table[low:j] have key < k
            (ii) All items of slice table[j:high+1] have key >= k
        """

        if high < low:
            return high + 1
        else:
            mid = (low + high) // 2
            if self._table[mid]._key == k:
                return mid
            elif self._table[mid]._key > k:
                return self._find_index(k, low, mid - 1)
            else:
                return self._find_index(k, mid + 1, high)

    def __init__(self):
        """Initialize an empty sorted map."""
        self._table = list()

    # ----- Inherited Abstract Methods ----- #

    def __setitem__(self, k, v):
        pass

    def __getitem__(self, k):
        pass

    def __delitem__(self, v):
        pass

    def __len__(self):
        pass

    def __iter__(self):
        pass

    # ----- Sorted Map ADT Methods ----- #

    def find_min(self):
        pass

    def find_max(self):
        pass

    def find_lt(self, k):
        pass

    def find_le(self, k):
        pass

    def find_gt(self, k):
        pass

    def find_ge(self, k):
        pass

    def find_range(self, start, stop):
        pass

    def __reversed__(self):
        pass
