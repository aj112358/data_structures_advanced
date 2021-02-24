"""An implementation of a queue with an array as the underlying structure.

Created By: AJ Singh
Date: Feb 23, 2021
"""


class Empty(Exception):
    """The error to raise when attempting to access an element from an empty stack."""
    pass


class ArrayQueue:
    """An implementation of a queue using arrays."""

    def __init__(self, N=10, size=0, front=0):
        """Instantiating a new queue."""

        self._N = N

        self._data = [] * N  # List instance to store the queue elements.
        self._size = size    # Integer representing the actual number of elements in the queue.
        self._front = front  # Integer representing the index of the 'first' queue element.

    def __len__(self):
        """Return the actual number of elements in the queue."""
        return self._size

    def is_empty(self):
        """Return True if the queue contains no elements."""
        return self._size == 0

    def first(self):
        """Returns the element at the front of the queue."""
        return self._data[self._front]

    def dequeue(self):
        """Removes and returns the front element of the queue."""

        if self.is_empty():
            raise Empty("The queue contains no elements.")

        self._size -= 1
        elem = self._data[self._front]
        self._data[self._front] = None
        self._front = (self._front + 1) % self._N



    def enqueue(self, e):
        """Adds element 'e' to the back of the queue."""


