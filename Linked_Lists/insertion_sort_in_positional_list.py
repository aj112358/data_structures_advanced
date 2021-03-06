"""This module gives an implementation of the insertion sort algorithm for a positional list.

Created By: AJ Singh
Date: March 6, 2021
"""


def insertion_sort(L):
    """Sorts elements of a positional list into non-decreasing order."""

    if len(L) > 1:

        marker = L.first()
        while marker != L.last():
            pivot = L.after(marker)
            value = pivot.element()

            if value > marker.element():  # Current pivot element is already sorted.
                marker = pivot
            else:
                walk = marker
                while walk != L.first() and L.before(walk).element() > value:
                    walk = L.before(walk)
                L.delete(pivot)
                L.add_before(walk, value)  # Insert value before 'walk' position.
