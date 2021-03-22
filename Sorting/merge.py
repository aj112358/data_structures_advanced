"""This module provides the basic function that merges already-sorted arrays.

Created By: AJ Singh
Date: March 22, 2021
"""


def merge(s1, s2, s=None):
    """Given sorted arrays s1 & s2, merge them together into array s."""

    if s is None:
        s = [None] * (len(s1) + len(s2))

    i = j = 0
    while i + j < len(s1) + len(s2):

        # Not all s1 elements have been used.
        if i < len(s1) and (j == len(s2) or (s1[i] < s2[j])):
            s[i + j] = s1[i]
            i += 1

        # All s1 elements have been used OR i-element is larger than j-element.
        else:
            s[i + j] = s2[j]
            j += 1

    return s


if __name__ == "__main__":
    s1 = [2, 5, 8, 11]
    s2 = [3, 9, 10, 18, 20]
    print(*merge(s1, s2), sep=" ")

    s1 = [2, 5, 8, 11, 20]
    s2 = [3, 9, 10, 18]
    print(*merge(s1, s2), sep=" ")

    s1 = [2, 5, 8, 11, 15]
    s2 = [3, 9, 10, 18]
    print(*merge(s1, s2), sep=" ")

    s1 = [2, 5, 8, 20]
    s2 = [3, 9, 10, 11, 18]
    print(*merge(s1, s2), sep=" ")

    s1 = [2, 5, 8, 11]
    s2 = [3, 9, 10, 18]
    print(*merge(s1, s2), sep=" ")