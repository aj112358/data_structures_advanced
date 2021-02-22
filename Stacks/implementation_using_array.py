"""An implementation of a stack using arrays.

Created By: AJ Singh
Date: Feb 22, 2021
"""


class Empty(Exception):
    """The error to raise when attempting to access an element from an empty stack."""
    pass


class ArrayStack:
    """Implementation of a LIFO stack using an array."""

    def __init__(self):
        """Create a new empty stack."""
        self._stack = []

    def push(self, e):
        """Add a new element 'e' to the top of the stack."""
        self._stack.append(e)

    def pop(self):
        """Remove and return the top element of the stack."""

        if self.is_empty():
            raise Empty("The stack contains no elements.")
        return self._stack.pop()

    def top(self):
        """Returns a reference to the top element of a stack."""

        if self.is_empty():
            raise Empty("The stack contains no elements.")
        return self._stack[-1]

    def is_empty(self):
        """Check whether a stack contains any elements."""
        return len(self._stack) == 0

    def __len__(self):
        """Return the number of elements in a stack."""
        return len(self._stack)

