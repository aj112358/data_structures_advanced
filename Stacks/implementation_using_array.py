"""An implementation of a stack using arrays.

Created By: AJ Singh
Date: Feb 22, 2021
"""


class Empty(Exception):
    """The error to raise when attempting to access an element from an empty stack."""
    pass


class ArrayStack:
    """Implementation of a stack using an array."""

    def __init__(self):
        """Create a new empty stack."""

        self._stack = []
        self._n = 0

    def push(self, e):
        """Add a new element 'e' to the top of the stack."""
        self._n += 1
        self._stack.append(e)

    def pop(self):
        """Remove and return the top element of the stack."""

        if self._n > 0:
            self._n -= 1
            return self._stack.pop()
        raise Empty

    def top(self):
        """Returns a reference to the top element of a stack."""
        return self._stack[-1]

    def is_empty(self):
        """Check whether a stack contains any elements."""
        return self._n == 0

    def __len__(self):
        """Return the number of elements in a stack."""
        return self._n

