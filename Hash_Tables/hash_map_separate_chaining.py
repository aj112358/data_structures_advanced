"""Implementing a hash map using separate chaining for collision handling, taken from book.

Created By: AJ Singh
Date: April 16, 2021
"""

from unsorted_map import UnsortedMap
from hash_map_base_class import HashMapBase


class ChainHashMap(HashMapBase):
    """A hash map implementation using separate chaining for collision handling."""

    def _bucket_setitem(self, j, k, v):

        # Check if hash table at key k currently has a container.
        # If not, create a new container, which is simply an unsorted map (collection of _Item objects).
        if self._table[j] is None:
            self._table[j] = UnsortedMap()

        oldsize = len(self._table[j])

        self._table[j][k] = v

        # Increment size if (k,v) element is new element (not just overwriting existing value).
        if len(self._table[j]) > oldsize:
            self._size += 1  # Increment number of unique entries in map.

    def _bucket_getitem(self, j, k):

        bucket = self._table[j]
        if bucket is None:
            raise KeyError("Key Error: " + repr(k))
        return bucket[k]

    def _bucket_delitem(self, j, k):

        bucket = self._table[j]
        if bucket is None:
            raise KeyError("Key Error: " + repr(k))
        del bucket[k]
        self._size -= 1

    def __iter__(self):
        pass
