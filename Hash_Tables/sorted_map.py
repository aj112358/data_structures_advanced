"""An implementation of a "sorted map", where the keys are sorted using the natural ordering on the keys, taken from
book.

Created By: AJ Singh
Date: April 18, 2021
"""
from typing import Iterator, _T_co, _KT, _VT_co, _VT

from hash_map_base_class import MapBase


class SortedTableMap(MapBase):
    """A map implementation using a sorted array."""

    # ----- Non-Public Utility Method ----- #
    def _find_index(self, k, low, high):
        pass

    def __init__(self):
        pass

    # ----- Inherited Abstract Methods ----- #

    def __setitem__(self, k: _KT, v: _VT) -> None:
        pass

    def __getitem__(self, k: _KT) -> _VT_co:
        pass

    def __delitem__(self, v: _KT) -> None:
        pass

    def __len__(self) -> int:
        pass

    def __iter__(self) -> Iterator[_T_co]:
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
