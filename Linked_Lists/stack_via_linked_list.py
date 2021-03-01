"""This is an implementation of the stack ADT with a (singly) linked list as the underlying structure.

Created By: AJ Singh
Date: March 1, 2021
"""


class LinkedStack:
    """An implementation for a FILO stack, using a singly linked list as the underlying structure."""

    class _Node:
        """Lightweight, non-public class for storing a singly linked node."""

        __slots__ = "_element", "_next"

        def __init__(self, element, next):
            """Creating a new node for the linked list."""
            self._element = element
            self._next = next

    def __init__(self):
        """Creating a new empty linked list object."""
        self._head = self._Node(None, None)
        self._size = 0

    def push(self, e):


    def pop(self):


    def peek(self):


    def __len__(self):
        

    def is_empty(self):



if __name__ == "__main__":
    print("Hello world")