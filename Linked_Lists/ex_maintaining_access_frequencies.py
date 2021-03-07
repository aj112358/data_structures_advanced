"""This module implements a class for maintaining access frequencies of a collection of objects, taken from book.

Created By: AJ Singh
Date: March 7, 2021
"""

from positional_list import PositionalList


class FavoritesList:
    """A list of elements ordered from most frequently accessed to least."""

    # ----- Class to store an element's value and access frequency. ----- #
    class _Item:
        """Object to store elements' value and access counts."""

        def __init__(self, e):
            self._value = e  # Element.
            self._count = 0  # To store access count.

    # ----- Non-public Utilities ----- #
    def _find_position(self, e):
        pass

    def _move_up(self, p):
        pass

    # ----- Public Methods ----- #
    def __init__(self):
        pass

    def __len__(self):
        pass

    def is_empty(self):
        pass

    def access(self, e):
        pass

    def remove(self, e):
        pass

    def top(self, k):
        pass

