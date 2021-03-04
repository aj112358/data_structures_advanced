"""An implementation of a queue using a circularly linked list.

Created By: AJ Singh
Date: March 3, 2021
"""

from Stacks.implementation_using_array import Empty


class CircularQueue:
    """An implementation of a queue ADT, using a circularly linked list as the underlying structure."""

    class _Node:
        """Lightweight, non-public class for storing a singly linked node."""

        __slots__ = "_element", "_next"

        def __init__(self, element, next):
            """Creating a new node for the linked list."""
            self._element = element
            self._next = next

    def __init__(self):
        """Instantiating an empty queue."""
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
        head = self._tail._next
        return head._element

    def enqueue(self, e):
        """Add new element 'e' to back of the queue (ie. tail of the linked list)."""
        new = self._Node(e, None)

        if self._size == 0:
            new._next = new
        else:
            new._next = self._tail._next  # Assigning this new tail's 'next' to the head.
            self._tail._next = new  # Re-assigning current tail's 'next' pointer to this new node.

        self._tail = new
        self._size += 1

    def dequeue(self):
        """Remove and return the first element in queue (ie. head of linked list)."""
        if self._size == 0:
            raise Empty("No elements in queue.")

        head = self._tail._next
        elem = head._element
        self._size -= 1

        if self._size == 0:
            self._tail = None  # Need to manually make the tail be 'None' if queue is now empty!
        else:
            self._tail._next = head._next

        return elem

    def _rotate(self):
        """Performs the operation of shifting the front node to the back of the queue."""
        if not self.is_empty():
            self._tail = self._tail._next  # The old head now becomes the new tail.
