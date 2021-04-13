"""Implementation of unsorted map, using a list and inheriting from MapBase base class.

Created By: AJ Singh
Date: April 12, 2021
"""
from typing import Iterator, _T_co, _KT, _VT_co, _VT

from map_abc import MapBase


class UnsortedMap(MapBase):
    """Map implementation using an unordered list."""

    def __init__(self):
        pass

    def __getitem__(self, k: _KT) -> _VT_co:
        pass

    def __setitem__(self, k: _KT, v: _VT) -> None:
        pass

    def __delitem__(self, v: _KT) -> None:
        pass

    def __len__(self) -> int:
        pass

    def __iter__(self) -> Iterator[_T_co]:
        pass
