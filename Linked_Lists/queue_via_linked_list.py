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



    def __len__(self):
        pass

    def is_empty(self):
        pass

    def first(self):
        pass

    def enqueue(self, e):
        pass

    def dequeue(self):
        pass


if __name__ == "__main__":
    print("Hello World")
