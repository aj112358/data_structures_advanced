"""This is a generic implementation of a doubly linked list.

It will be used as a parent class for:
    - a deque implemented using a doubly linked list
    - a "Positional ADT"

Created By: AJ Singh
Date: Mar 4, 2021
"""

# This import is not needed! Because we will always have at least the sentinel nodes!
# from Stacks.implementation_using_array import Empty


class _DoublyLinkedBase:
    """A base class for a doubly linked list."""

    class _Node:
        """Lightweight, non-public class for storing a double linked node."""

        __slots__ = "_element", "_next", "_prev"

        def __init__(self, element, prev, next):
            """Creating a new node for the linked list."""
            self._element = element
            self._prev = prev
            self._next = next

    def __init__(self):
        """Creating a new empty doubly linked list."""

        # Sentinel nodes.
        self._header = self._Node(None, None, None)
        self._trailer = self._Node(None, None, None)

        # Point to one another initially.
        self._header._next = self._trailer
        self._trailer._prev = self._header

        self._size = 0  # Maintain reference to current number of non-sentinel (ie. element) nodes.

    def __len__(self):
        """Returns the current number of element nodes in a doubly linked list."""
        return self._size

    def is_empty(self):
        """Returns True if there are no element nodes; else returns False."""
        return self._size == 0

    def _insert_between(self, e, predecessor, successor):
        """Insert element 'e' in between the predecessor and successor nodes."""

        new = self._Node(e, predecessor, successor)

        # Re-assign links of adjacent nodes to the new node.
        predecessor._next = new
        successor._prev = new

        self._size += 1
        return new  # For convenience.

    # BETTER TO SIMPLY USE THE NODE IN QUESTION!!!! SEE IMPLEMENTATION BELOW
    # def _delete_node(self, predecessor, successor):
    #     """Delete the node between the predecessor and successor nodes."""
    #
    #     predecessor._next._prev = None
    #     successor._prev._next = None
    #     predecessor._next._element = None
    #
    #
    #     predecessor._next = successor
    #     successor._prev = predecessor
    #     self._size -= 1

    def _delete_node(self, node):
        """Deletes 'node' (an element node; non-sentinel) from the linked list."""

        predecessor = node._prev
        successor = node._next

        # Re-assign links of adjacent nodes to each other.
        predecessor._next = successor
        successor._prev = predecessor
        self._size -= 1

        element = node._element  # Old element to return.

        # For Python garbage collection.
        node._prev = None
        node._next = None
        node._element = None

        return element  # For convenience.
