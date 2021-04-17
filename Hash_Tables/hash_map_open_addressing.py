"""Implementing a hash map, using open addressing (via linear probing) for collision handling, taken from book.

Created By: AJ Singh
Date: April 16, 2021
"""

from hash_map_base_class import HashMapBase


class ProbeHashMap(HashMapBase):
    """A hash map that uses open addressing (linear probing) for collision handling."""

    # ----- Non-Public Utility Methods ----- #

    # Sentinel to mark slots with prior elements that were deleted.
    # Using Python's built-in 'object' class to define generic objects.
    _AVAILABLE = object()

    # Determine if slot in hash table is content-free.
    def _is_available(self, j):
        """Return True if slot at index j is available in the hash table."""
        bucket = self._table[j]
        if bucket in {None, ProbeHashMap._AVAILABLE}:
            return True
        return False

    def _find_slot(self, j, k):
        """Search for key k in bucket at index j. Note: The key may not be located at index j literally (because of
        linear probing).

        @return: Tuple (success, index) defined as:
            - If match is found, 'success' is True & 'index' is the found location.
            - If match not found, 'success' is False & 'index' will be the first available slot.
        """

        first_avail = None  # Initializing sentinel for indices.
        while True:
            if self._is_available(j):

                if first_avail is None:
                    first_avail = j

                # The case when there was never an existing element at bucket j.
                # So, we are checking to see if an existing element was previously removed.
                # If NOT (ie. None), then this bucket never contained an element, hence we
                # do not have to continue searching subsequent buckets.
                # BUT: If bucket DID contain a (now deleted) element, this means we have to
                # continue to check subsequent buckets, hence this code block won't run.
                # Look at notes on linear probing to review more details.
                if self._table[j] is None:
                    return False, first_avail

            # If the bucket is not available, check if the stored key matches input key.
            # In this case, we would have to reassign the key value.
            elif self._table[j]._key == k:
                return True, j

            j = (j+1) % len(self._table)

    # ----- Concrete Methods ----- #

    def _bucket_setitem(self, j, k, v):
        pass

    def _bucket_getitem(self, j, k):
        pass

    def _bucket_delitem(self, j, k):
        pass

    def __iter__(self):
        pass

