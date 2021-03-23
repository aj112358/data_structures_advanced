"""An implementation of sorting a linked list using the merge-sort algorithm.

Uses a queue data structure implemented using an underlying linked list.

Created By: AJ Singh
Date: March 23, 2021
"""

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