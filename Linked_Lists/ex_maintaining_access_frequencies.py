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
        __slots__ = "_value", "_count"
        def __init__(self, e):
            self._value = e  # Element.
            self._count = 0  # To store access count.

    # ----- Non-Public Utilities ----- #
    def _find_position(self, e):
        """Search for element 'e' and return its position, or None if not found."""

        walk = self._data.first()  # Start at header of underlying linked list.
        while (walk is not None) and (walk.element()._value != e):
            walk = self._data.after(walk)
        return walk

    def _move_up(self, p):
        """Move item at position 'p' *earlier* in the list, based on access counts."""

        if p != self._data.first():

            count = p.element()._count()
            walk = self._data.before(p)
            if count > walk.element()._count:  # Need to shift element forward/up the positional list.

                # You're not at the head of the LL & Current count is larger than next count.
                while (walk != self._data.first()) and (count > self._data.before(walk).element()._count):
                    walk = self._data.before(walk)  # Continue backward traversal through linked list.

                self._data.add_before(walk, self._data.delete(p))  # Insert element at correct position in list.

    # ----- Public Methods ----- #
    def __init__(self):
        """Create an empty list of favorites."""
        self._data = PositionalList()  # Will be a list of _Item instances (from nested class above)

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
