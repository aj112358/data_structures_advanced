"""This is an implementation of the FIFO queue ADT with a (singly) linked list as the underlying structure.

Created By: AJ Singh
Date: March 1, 2021
"""

from Stacks.implementation_using_array import Empty


class LinkedQueue:
    """An implementation of a FIFO queue ADT, using a linked list as the underlying structure."""

    class _Node:
        """Lightweight, non-public class for storing a singly linked node."""

        __slots__ = "_element", "_next"

        def __init__(self, element, next):
            """Creating a new node for the linked list."""
            self._element = element
            self._next = next

    def __init__(self):
        """Instantiating an empty queue."""
        self._head = None   # Reference to FRONT of the queue.
        self._tail = None   # Reference to BACK of the queue.
        self._size = 0      # Maintains number of elements in the queue.

    def __len__(self):
        """Return the number of elements in the queue."""
        return self._size

    def is_empty(self):
        """Return True if no elements in queue; else return False."""
        return self._size == 0

    def first(self):
        """Return (but not remove) the current first element in the queue."""
        if self._size == 0:
            raise Empty("No elements in queue.")
        return self._head._element

    def enqueue(self, e):
        """Add new element 'e' to back of the queue (ie. tail of the linked list)."""
        new = self._Node(e, None)

        if self._size == 0:
            self._head = new
        else:
            self._tail._next = new  # If queue is not empty, re-assign old tail reference to reference the new node.

        self._tail = new  # Re-assign tail as new node.
        self._size += 1

    def dequeue(self):
        """Remove and return the first element in queue (ie. head of linked list)."""
        if self._size == 0:
            raise Empty("No elements in queue.")

        elem = self._head._element
        self._head = self._head._next  # Will become 'None' if queue is now empty!
        self._size -= 1

        if self._size == 0:
            self._tail = None  # Need to manually make the tail be 'None' if queue is now empty!

        return elem


if __name__ == "__main__":

    q = LinkedQueue()
    print(len(q))

    q.enqueue("First")
    q.enqueue("Second")
    print(len(q))
    print(q.first())
    print()

    q.enqueue("Third")
    print(q.dequeue())
    print(q.dequeue())
    print(q.is_empty())
    print()

    print(q.dequeue())
    print(q.is_empty())
    print(q.first())
