"""An implementation of the quick-sort algorithm as an in-place algorithm via arrays, taken from book.

Created By: AJ Singh
Date: March 27, 2021
"""


def quick_sort_inplace(s, a, b):
    """Sort an array 's' between indices a & b (inclusive) in-place using the quick-sort algorithm."""

    if a >= b:
        return

    left = a
    right = b - 1

    pivot = s[b]  # Selecting last element as pivot.
    while left <= right:

        while left <= right and s[left] < pivot:
            left += 1
        while left <= right and s[right] > pivot:
            right -= 1

        if left <= right:
            s[left], s[right] = s[right], s[left]  # Swapping values.
            left, right = left+1, right-1          # Shrinking range to check.

    s[left], s[b] = s[b], s[left]  # Put pivot into its respective place.

    quick_sort_inplace(s, a, left-1)
    quick_sort_inplace(s, left+1, b)


if __name__ == "__main__":
    seq = [50, 85, 24, 63, 45, 17, 31, 96]

    print("Original:")
    print(*seq, sep=" ")

    quick_sort_inplace(seq, 0, 7)

    print("\n\nSorted:")
    print(*seq, sep=" ")
