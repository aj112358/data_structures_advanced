"""An implementation of a positional list, taken from book.

Created By: AJ Singh
Date: March 5, 2021
"""

from doubly_linked_list_base_class import _DoublyLinkedBase
from Stacks.implementation_using_array import Empty


class PositionalList:
    """A sequential container of elements allowing positional access."""

    # Objects to represent position of a node.
    class Position:
        """An abstraction representing the location of a single element."""

        def __init__(self, container, node):
            """Constructor should NOT be invoked by user!"""
            self._container = container
            self._node = node

        def element(self):
            """Return the element stored at specified position."""
            return self._node._element

        def __eq__(self, other):
            """Return True if other is a Position representing the same location."""
            # Using 'is' keyword to compare physical memory references.
            return (type(other) is type(self)) and (other._node is self._node)

        def __ne__(self, other):
            """Return True if 'other' does not represent the same location."""
            return not (self == other)

    # All utility methods.

    def _validate(self, p):
        """Return node at position 'p', or raise error if position is invalid."""

        if not isinstance(p, self.Position):
            raise TypeError("Given parameter must be of type Position.")

        if p._container is not self:
            raise ValueError("Given position parameter does not belong to this container.")

        if p._node._next is None:
            raise ValueError("Given position is no longer valid.")

        return p._node

    def _make_position(self, node):
        """Return node's Position instance, or None if node is a sentinel."""

        if (node is self._header) or (node is self._trailer):
            return None
        return self.Position(self, node)

    # All accessor methods.

    def first(self):
        pass

    def last(self):
        pass

    def before(self, p):
        pass

    def after(self, p):
        pass

    def is_empty(self):
        pass

    def __len__(self):
        pass

    def __iter__(self):
        pass