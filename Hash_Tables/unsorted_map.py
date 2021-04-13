"""Implementation of unsorted map, using a list and inheriting from MapBase base class.

Created By: AJ Singh
Date: April 12, 2021
"""

from map_abc import MapBase


class UnsortedMap(MapBase):
    """Map implementation using an unordered list."""

    def __init__(self):
        """Create an empty map."""
        self._table = list()

    def __setitem__(self, k, v):
        """Assign value v to key k, or re-assign if key k already exists."""

        for item in self._table:  # Check if key k exists.
            if item._key == k:
                item._value = v
                return

        new_item = self._Item(k, v)  # Add key-value pair if key doesn't exist.
        self._table.append(new_item)

    def __getitem__(self, k):
        """Return value associated with key k; raise KeyError if does not exist."""

        for item in self._table:
            if item._key == k:
                return item._value
        else:
            raise KeyError("Key {0} does not exist in map.".format(k))

    def __delitem__(self, k):
        """Remote the item associated with key k; raise KeyError if doesn't exist."""

        for index, item in enumerate(self._table):
            if item._key == k:
                self._table.pop(index)
        else:
            raise KeyError("Key {0} does not exist in map.".format(k))

    def __len__(self):
        """Return number of items in the map."""
        return len(self._table)

    def __iter__(self):
        pass


if __name__ == "__main__":

    x = UnsortedMap()
    x["a"] = 1
    print(x["a"])
    x["b"]