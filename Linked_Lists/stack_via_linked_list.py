"""This is an implementation of the stack ADT with a (singly) linked list as the underlying structure.

Created By: AJ Singh
Date: March 1, 2021
"""

from Stacks.implementation_using_array import Empty


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
        # self._head = self._Node(None, None)
        self._head = None  # Stores reference to head of linked list (ie. top of stack).
        self._size = 0     # Stores the number of elements in the stack.

    def push(self, e):
        """Add new element 'e' to top of the stack."""
        self._head = self._Node(e, self._head)  # Essentially removing the current head node, and replacing with next.
        self._size += 1

    def pop(self):
        """Remove and return the top element of the stack."""

        if self._size == 0:
            raise Empty("No elements in the stack.")

        elem = self._head._element  # Element at top of stack to return.
        self._head = self._head._next  # Re-assigning head of linked list to the new top element of stack.
        self._size -= 1

        return elem

    def peek(self):
        """Return (but not remove) the top element of the stack."""

        if self._size == 0:
            raise Empty("No elements in the stack.")
        return self._head._element

    def __len__(self):
        """Return number of elements in the stack."""
        return self._size

    def is_empty(self):
        """Returns True if stack has no elements; else returns False."""
        return self._size == 0


if __name__ == "__main__":

    stack = LinkedStack()
    print(len(stack))

    stack.push("hello")
    stack.push("world")
    print(len(stack))

    x = stack.pop()
    print(x)
    print(len(stack))
    print("Current top element:", stack.peek())
    print(stack.is_empty())

    print()
    print(stack.pop())
    print(len(stack))

    stack.pop()
