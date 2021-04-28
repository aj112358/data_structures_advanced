"""Using a priority queue to sort elements in a positional list.

Created By: AJ Singh
Date: April 28, 2021
"""

from priority_queue_unsorted import UnsortedPriorityQueue
from Linked_Lists.positional_list import PositionalList


def pq_sort(container):
    """Sort a collection of elements in-place that are stored in a positional list."""

    n = len(container)
    pq = UnsortedPriorityQueue()

    # Add elements to the priority queue.
    for j in range(n):
        elem = container.delete(container.first())
        pq.add(elem, elem)  # Using the element as both the key and value.

    # Extract elements from priority queue and insert back into the original container in sorted order.
    for j in range(n):
        k, v = pq.remove_min()
        container.add_last(v)


if __name__ == "__main__":
    x = [5, 4, 35, 2, 1, 200]

    pos_list = PositionalList()
    for _ in range(len(x)):
        pos_list.add_first(x.pop())

    pq_sort(pos_list)

    for elem in pos_list:
        print(elem, end=" ")
