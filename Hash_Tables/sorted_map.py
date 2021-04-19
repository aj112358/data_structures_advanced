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
        """Assigns value v to key k; overwrites value if key already exists."""

        index = self._find_index(k, 0, len(self._table)-1)

        if index < len(self._table) and self._table[index]._key == k:
            self._table[j]._value = k
        else:
            self._table.insert(__index=index, __object=v)

    def __getitem__(self, k):
        """Return value associated with key k; else raise KeyError if key not in map."""

        index = self._find_index(k, 0, len(self._table)-1)

        if index == len(self._table) or self._table[index]._key != k:
            raise KeyError("Key not found. Key Error: " + repr(k))
        return self._table[index]._value

    def __delitem__(self, k):
        """Remove item associated with key k; raise KeyError if key not in map. Doesn't return anything."""

        index = self._find_index(k, 0, len(self._table) - 1)

        if index == len(self._table) or self._table[index]._key != k:
            raise KeyError("Key not found. Key Error: " + repr(k))
        self._table.pop(index)

    def __len__(self):
        """Return number of items in map."""
        return len(self._table)

    def __iter__(self):
        """Generate keys of the map ordered from smallest to largest (as per the natural ordering of the keys)."""

        for item in self._table:
            yield item._key

    # ----- Sorted Map ADT Methods ----- #

    def find_min(self):
        """Return key-value pair with the minimum key."""
        if len(self._table) > 0:
            return self._table[0]._key, self._table[0]._value
        return None

    def find_max(self):
        """Return key-value pair with the maximum key."""
        if len(self._table) > 0:
            return self._table[-1]._key, self._table[-1]._value
        return None

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
