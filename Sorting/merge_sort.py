"""An implementation of the usual merge-sort algorithm.

Created By: AJ Singh
Date: March 22, 2021
"""

from merge import merge
from math import floor


def merge_sort(s):
    """Sorts the elements in array 's' using the merge-sort algorithm.

    Sorting is done in-place.
    """

    if len(s) in {0, 1, 2, 3}:
        return s.sort()

    mid = floor(len(s) / 2)

    s1 = s[:mid]
    s2 = s[mid:]

    merge_sort(s1)
    merge_sort(s2)

    merge(s1, s2, s)

    return s


if __name__ == "__main__":
    x = [1, 3, 2, 4, 6, 5, 8, 7]
    print(merge_sort(x), sep=" ")
    print(*x, sep=" ")

    y = [2, 1, 3]
    # print(*merge_sort(y), sep=" ")
    merge_sort(y)
    print(*y, sep=" ")

    z = [-1, 3, -2, 4, -6, 5, -8, 7]
    # print(*merge_sort(y), sep=" ")
    merge_sort(z)
    print(*z, sep=" ")
