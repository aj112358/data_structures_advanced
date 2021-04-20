"""An implementation of a multi-set (can contain duplicate elements).

Created By: AJ Singh
Date: April 20, 2021
"""


class MultiMap:
    """A multimap class built upon use of an underlying map for storage."""

    _MapType = dict  # Data structure to use to contain elements; Can be overridden by subclassing.

    def __init__(self):
        """Create a new empty multimap instance."""
        self._map = self._MapType()
        self._n = 0

    def add(self, k, v):
        """Add pair (k,v) to multimap."""
        # if k not in self._map:
        #     self._map[k] = list()
        # self._map[k].append(v)

        container = self._map.setdefault(k, list())
        container.append(v)
        self._n += 1

    def pop(self, k):
        pass

    def find(self, k):
        pass

    def find_all(self, k):
        pass

    def __iter__(self):
        pass