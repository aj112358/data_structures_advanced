"""Extending the original "MapBase" abc to include the commonality between using separate chaining and open addressing
(two collision handling schemes).

Created By: AJ Singh
Date: April 15, 2021
"""

from map_abc import MapBase


class HashMapBase(MapBase):
    """ABC for a map implemented with a hash table, using MAD compression."""

    def __init__(self):
        pass

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
