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

    while not s.is_empty():
        elem = s.first()
        if elem < pivot:
            less.enqueue(s.dequeue())
        elif elem > pivot:
            greater.enqueue(s.dequeue())
        else:
            equal.enqueue(s.dequeue())

    # print("Less elements")
    # while not less.is_empty():
    #     print(less.dequeue())

    quick_sort(less)
    quick_sort(greater)

    while not less.is_empty():
        s.enqueue(less.dequeue())
    while not equal.is_empty():
        s.enqueue(equal.dequeue())
    while not greater.is_empty():
        s.enqueue(greater.dequeue())

    # while not s.is_empty():
    #     print(s.dequeue())

    return s


if __name__ == "__main__":
    seq = LinkedQueue()
    elements = [50, 85, 24, 63, 45, 17, 31, 96]

    print("Original:")
    for _ in elements:
        seq.enqueue(_)
        print(_, end=" ")

    quick_sort(seq)

    print("\n\nSorted:")
    while len(seq) != 0:
        print(seq.dequeue(), end=" ")
