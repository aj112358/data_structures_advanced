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
        self._prime = prime                   # Prime number needed for MAD compression.
        self._scale = 1 + randrange(prime-1)  # Scale needed for MAD.
        self._shift = randrange(prime)        # Shift needed for MAD.

    def _hash_function(self):
        pass

    def __len__(self) -> int:
        pass

    def __setitem__(self, k: _KT, v: _VT) -> None:
        pass

    def __getitem__(self, k: _KT) -> _VT_co:
        pass

    def __delitem__(self, v: _KT) -> None:
        pass

    def _resize(self):
        pass
