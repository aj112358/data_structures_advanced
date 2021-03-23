"""This module provides the basic function that merges already-sorted arrays.

Created By: AJ Singh
Date: March 22, 2021
"""


def merge(s1, s2, s=None):
    """Given sorted arrays s1 & s2, merge them together into array s.

    Returns the combined sorted array.
    """

    if s is None:
        s = [None] * (len(s1) + len(s2))

    i = j = 0
    while i + j < len(s1) + len(s2):

        # # Not all s1 elements have been used.
        # if i < len(s1) and (j == len(s2) or (s1[i] < s2[j])):
        #     s[i + j] = s1[i]
        #     i += 1

        # This is better than above due to short-circuiting!
        if j == len(s2) or (i < len(s1) and s1[i] < s2[j]):
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

    s1 = [2, 5, 8, 11, 18]
    s2 = [3, 9, 10, 20]
    print(*merge(s1, s2), sep=" ")

    s1 = [2, 5, 8, 20]
    s2 = [3, 9, 10, 11, 18]
    print(*merge(s1, s2), sep=" ")

    s1 = [2, 5, 8, 11]
    s2 = [3, 9, 10, 18]
    print(*merge(s1, s2), sep=" ")

    s1 = [2, 5, 8, 11]
    s2 = [3, 5, 10, 11]
    print(*merge(s1, s2), sep=" ")
