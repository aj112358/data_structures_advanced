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
        self._n = 0  # Total number of elements in set (including duplicates)

    def add(self, k, v):
        """Add pair (k,v) to multimap."""
        # if k not in self._map:
        #     self._map[k] = list()
        # self._map[k].append(v)

        container = self._map.setdefault(k, list())
        container.append(v)
        self._n += 1

    def pop(self, k):
        """Remove and return an arbitrary (k,v) item, or raise KeyError if set is empty or key k does not exist."""
        if self._n == 0:
            raise KeyError("Set is empty.")

        container = self._map[k]  # Will raise KeyError if k not in set. Gets all values associated with key k.
        v = container.pop()       # Return an arbitrary value. (BUT in new versions of Python, will only return last value?)

        if len(container) == 0:   # Check if key has any remaining values.
            del self._map[k]      # If not, can remove key from set.
        self._n -= 1
        return k, v

    def find(self, k):
        """Return 'arbitrary' (k,v) item with key k, or raise KeyError if k does not exist."""

        container = self._map[k]  # May raise KeyError.
        v = container[0]
        return k, v

    def find_all(self, k):
        """Generate iteration of all (k,v) pairs with key k."""
        container = self._map.get(k, list())
        for v in container:
            yield k, v

    def __iter__(self):
        pass