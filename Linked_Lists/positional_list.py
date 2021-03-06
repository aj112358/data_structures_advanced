"""An implementation of a positional list, taken from book.

Created By: AJ Singh
Date: March 5, 2021
"""

from doubly_linked_list_base_class import _DoublyLinkedBase
from Stacks.implementation_using_array import Empty


class PositionalList(_DoublyLinkedBase):
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
        """Return Position of first element, or None if positional list is empty."""
        return self._make_position(self._header._next)

    def last(self):
        """Return Position of last element, or None if positional list is empty."""
        return self._make_position(self._trailer._next)

    def before(self, p):
        """Return Position just before Position p, or None if p is first."""
        node = self._validate(p)
        return self._make_position(node._prev)

    def after(self, p):
        """Return Position just after Position p, or None if p is first."""
        node = self._validate(p)
        return self._make_position(node._next)

    def __iter__(self):
        """Generate a forward iteration of elements of positional list."""
        cursor = self.first()
        while cursor is not None:
            yield cursor.element()
            cursor = self.after(cursor)

    ## __len__ method inherited from super class.
    # def __len__(self):
    #     pass

    ## Inherited from super class.
    # def is_empty(self):
    #     pass

    # All mutator methods

    # Overriding inherited version to return Position, instead of Node

    def _insert_between(self, e, predecessor, successor):
        """Add element between existing nodes and return new Positions."""
        node = super()._insert_between(e, predecessor, successor)
        return self._make_position(node)

    def add_first(self, e):
        """Insert element 'e' at the front of the positional list, and return its new Position."""
        self._insert_between(e, self._header, self._header._next)

    def add_last(self, e):
        """Insert element 'e' at the back of the positional list, and return its new Position."""
        self._insert_between(e, self._trailer._prev, self._trailer)

    def add_before(self, p, e):
        """Insert element 'e' into positional list, right before Position p, and return its new position."""
        original = self._validate(p)
        return self._insert_between(e, original._prev, original)

    def add_after(self, p, e):
        """Insert element 'e' into positional list, right after Position p, and return its new position."""
        original = self._validate(p)
        return self._insert_between(e, original, original._next)

    def delete(self, p):
        """Remove and return the element at Position p."""
        node_to_delete = self._validate(p)
        # return super()._delete_node(node_to_delete)
        return self._delete_node(node_to_delete)
    
    def replace(self, p, e):
        pass