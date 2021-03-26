"""An implementation of the quick-sort algorithm that operates on any queue-based sequence.

Created By: AJ Singh
Date: March 26, 2021
"""

from Linked_Lists.queue_via_linked_list import LinkedQueue


def quick_sort(s):
    """Sorts the elements of the queue 's' using the quick-sort algorithm."""

    if len(s) in {0, 1}:
        return s

    pivot = s.first()

    less = LinkedQueue()
    equal = LinkedQueue()
    greater = LinkedQueue()

    elem = s.first()

    while elem is not None:

        if elem < pivot:
            less.enqueue(s.dequeue())
        elif elem > pivot:
            greater.enqueue(s.dequeue())
        else:
            equal.enqueue(s.dequeue())

        elem = elem.next()