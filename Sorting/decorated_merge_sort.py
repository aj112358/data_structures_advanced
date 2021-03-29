"""An implementation of the keyword argument 'key=' used in Python's built-in sorting functions, taken from book.

An illustration of the 'decorate-sort-undecorate' design pattern.

Created By: AJ Singh
Date: March 29, 2021
"""

from merge_sort import merge_sort


class _Item:
    """Lightweight composite to store key-value pairs."""
    __slots__ = '_key', '_value'

    def __init__(self, k, v):
        self._key = k
        self._value = v

    def __lt__(self, other):
        return self._key < other._key


def decorated_merge_sort(data, key=None):
    """Sort a sequence using merge-sort, and an optional 'key' to define how sorting should be done."""

    if key is not None:
        for j in range(len(data)):
            data[j] = _Item(k=key(data[j]), v=data[j])

    merge_sort(data)  # Can use any sorting function.

    if key is not None:
        for j in range(len(data)):
            data[j] = data[j]._value


if __name__ == "__main__":
    seq = ['red', 'green', 'blue', 'cyan', 'magenta', 'yellow']

    print("Original:")
    print(*seq, sep=" ")

    decorated_merge_sort(seq)
    print("\nSorted (via <):")
    print(*seq, sep=" ")

    decorated_merge_sort(seq, key=len)
    print("\nSorted (via length):")
    print(*seq, sep=" ")

    decorated_merge_sort(seq, key=lambda x: x[-1])
    print("\nSorted (via last character in string):")
    print(*seq, sep=" ")
