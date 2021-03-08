"""This module defines a class that implements a favorites list, using the "move-to-front" heuristic, taken from book.

Created By: AJ Singh
Date: March 7, 2021
"""

from ex_maintaining_access_frequencies import FavoritesList
from positional_list import PositionalList


class FavoritesListMTF(FavoritesList):
    """A list of elements, ordered as per the move-to-front heuristic."""

    # Overriding the _move_up() utility from base class, to implement MTF heuristic.
    def _move_up(self, p):
        """Moves accessed item from position 'p' to front of the list."""

        if p != self._data.first():
            elem = self._data.delete(p)
            self._data.add_first(elem)

    # Overriding top() method, because list is no longer sorted.
    def top(self, k):
        """Create generator for the top 'k' elements, with respect to access frequency."""

        if not 1 <= k <= len(self):
            raise ValueError("'k' value outside of range.")

        # Using a temporary list to store items from favorites list.
        temp = PositionalList()
        for item in self._data:
            temp.add_last(item)

        # Iteratively find 'k' most frequently accessed elements, and remove them.
        for i in range(k):

            high_pos = temp.first()  # Initializing first element as highest so far.
            walk = temp.after(high_pos)  # Initializing second element as one to compare with.

            # Must iterate through entire positional list!
            while walk is not None:
                if walk.element()._count > high_pos.element()._count:
                    high_pos = walk  # Updating highest position as we go.
                walk = temp.after(walk)  # Updating next element to be compared with.

            yield high_pos.element()._value  # Reporting current highest element to user.

            # Removing currently found highest element from temporary list, before iterating again.
            temp.delete(high_pos)
