"""Extending the original "MapBase" abc to include the commonality between using separate chaining and open addressing
(two collision handling schemes).

Created By: AJ Singh
Date: April 15, 2021
"""

from random import randrange
from map_abc import MapBase


class HashMapBase(MapBase):
    """ABC for a map implemented with a hash table, using MAD compression."""

    def __init__(self, capacity=11, prime=109345121):
        """Initializes a new empty hash table."""
        self._table = [None] * capacity
        self._size = 0                        # Number of unique entries in map.
        self._prime = prime                   # Prime number needed for MAD compression. (Should be larger than size).
        self._scale = 1 + randrange(prime-1)  # Scale needed for MAD.
        self._shift = randrange(prime)        # Shift needed for MAD.

    def _hash_function(self, i):
        """Using MAD method for compression. Uses Python's built-in hash function."""
        return ((self._scale * hash(i) + self._shift) % self._prime) % len(self._table)

    def __len__(self) -> int:
        return self._size

    def __setitem__(self, k, v):
        j = self._hash_function(k)
        self._bucket_setitem(j, k, v)  # Will maintain/update self._size

        # Check if load factor increases beyond 0.5
        if self._size > len(self._table) // 2:
            self._resize(2 * len(self._table) - 1)

    def __getitem__(self, k):
        j = self._hash_function(k)
        return self._bucket_getitem(j, k)

    def __delitem__(self, v: _KT) -> None:
        pass

    def _resize(self, capacity):
        pass
