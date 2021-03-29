"""An implementation to find the k-th smallest element in a collection.

Created By: AJ Singh
Date: March 29, 2021
"""

from random import choice


def quick_select(s, k):
    """Return the k-th smallest element from the list 's'."""

    if not 1 <= k <= len(s):
        raise ValueError("Value of k must be positive integer at most the length of sequence.")

    if len(s) == 1:
        return s[0]

    pivot = choice(s)

    less = [x for x in s if x < pivot]
    equal = [x for x in s if x == pivot]
    greater = [x for x in s if x > pivot]

    if k <= len(less):
        return quick_select(less, k)
    elif k <= len(less) + len(equal):
        return pivot
    else:
        j = k - len(less) - len(equal)
        return quick_select(greater, j)


if __name__ == "__main__":
    seq = [2, 3, 5, 7, 9, 4, 1, 6, 8]

    k = 5
    print(f"The {k}-th smallest element is:", quick_select(seq, k))