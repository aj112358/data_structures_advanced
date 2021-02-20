"""An implementation of the 'insertion sort' algorithm, taken from book.

Created By: AJ Singh
Date: Feb 20, 2021
"""


def insertion_sort(arr):
    """Sort a list (of comparable elements) in non-decreasing order."""

    for k in range(1, len(arr)):  # Checks all list elements.
        current = arr[k]

        j = k
        while j > 0 and arr[j - 1] > current:  # Compares current element with all elements to its left.
            arr[j] = arr[j - 1]  # Right-shifting.
            j -= 1

        arr[j] = current  # Insert the current element in the correct position.
