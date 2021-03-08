"""This module defines a class that implements a favorites list, using the "move-to-front" heuristic, taken from book.

Created By: AJ Singh
Date: March 7, 2021
"""

from ex_maintaining_access_frequencies import FavoritesList


class FavoritesListMTF(FavoritesList):
    """A list of elements, ordered as per the move-to-front heuristic."""

    # Overriding the _move_up() utility from base class, to implement MTF heuristic.
    def _move_up(self, p):
        """Moves accessed item from position 'p' to front of the list."""

        