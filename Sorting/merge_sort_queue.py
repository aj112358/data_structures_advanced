"""An implementation of sorting a queue data structure using the merge-sort algorithm.

Created By: AJ Singh
Date: March 23, 2021
"""

from math import floor
from Linked_Lists.queue_via_linked_list import LinkedQueue


def merge(s1, s2, s=None):
    """Merge two already-sorted queues s1 & s2."""

    if s is None:
        s = LinkedQueue()

    while (not s1.is_empty()) and (not s2.is_empty()):

        if s1.first() < s2.first():
            s.enqueue(s1.dequeue())
        else:
            s.enqueue(s2.dequeue())

    while not s1.is_empty():  # Merge any remaining elements in s1.
        s.enqueue(s1.dequeue())

    while not s2.is_empty():  # Merge any remaining elements in s2.
        s.enqueue(s2.dequeue())

    return s


def merge_sort(s):
    """Sort the elements of a queue 's' using the merge-sort algorithm."""

    if len(s) in {0, 1}:
        return s

    s1 = LinkedQueue()
    s2 = LinkedQueue()

    mid = floor(len(s) / 2)

    while len(s1) < mid:  # Transfer first half of elements in s to s1.
        s1.enqueue(s.dequeue())

    while not s.is_empty():  # Transfer second half of elements in s to s2.
        s2.enqueue(s.dequeue())

    merge_sort(s1)
    merge_sort(s2)

    merge(s1, s2, s)

    return s
