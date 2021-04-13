"""Implementing the ABC for our map class.

Created By: AJ Singh
Date: April 12, 2021
"""

from collections import MutableMapping


class MapBase(MutableMapping):
    """Abstract base class for map implementation.

    Extends MutableMapping class to include non-public _Item class.
    """

    class _Item:
        """Stores key-value pairs as map items."""

        __slots__ = "_key", "_value"

        def __init__(self, k, v):
            self._key = k
            self._value = v

        def __eq__(self, other):
            return self._key == other._key

        def __ne__(self, other):
            return not (self == other)

        def __lt__(self, other):
            return self._key < other._key
