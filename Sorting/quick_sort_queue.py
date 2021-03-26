"""An implementation of the quick-sort algorithm that operates on any queue-based sequence.

Created By: AJ Singh
Date: March 26, 2021
"""

from Linked_Lists.queue_via_linked_list import LinkedQueue


def quick_sort(s):
    """Sorts the elements of the queue 's' using the quick-sort algorithm."""

    if len(s) in {0, 1}:
        return

    pivot = s.first()

    less = LinkedQueue()
    equal = LinkedQueue()
    greater = LinkedQueue()

    elem = s.first()
    while not s.is_empty():
        if elem < pivot:
            less.enqueue(s.dequeue())
        elif elem > pivot:
            greater.enqueue(s.dequeue())
        else:
            equal.enqueue(s.dequeue())

        if len(s) == 0:
            break
        elem = s.first()

    quick_sort(less)
    quick_sort(greater)

    while len(less) != 0:
        s.enqueue(less.dequeue())
    while len(equal) != 0:
        s.enqueue(equal.dequeue())
    while len(greater) != 0:
        s.enqueue(greater.dequeue())

    print("HellO", len(s))

    # while len(s) != 0:
    #     print(s.dequeue(), end=" ")

    # return s


if __name__ == "__main__":
    seq = LinkedQueue()
    elements = [50, 85, 24, 63, 45, 17, 31, 96]

    for _ in elements:
        seq.enqueue(_)

    print("Original:")
    while len(seq) != 0:
        print(seq.dequeue(), end=" ")

    quick_sort(seq)

    print("\n\nSorted:")
    while len(seq) != 0:
        print(seq.dequeue(), end=" ")
