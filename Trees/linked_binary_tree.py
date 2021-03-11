"""A module that defines a binary tree using a linked structure, adapted from book.

Created By: AJ Singh
Date: March 11, 2021
"""

from binary_tree_abc import BinaryTree


class LinkedBinaryTree(BinaryTree):
    """A binary tree structure using a linked representation."""

    # Objects to represent physical tree nodes.
    class _Node:
        """Class for node objects."""

        __slots__ = "_element", "_parent", "_left", "_right"

        def __init__(self, element, parent=None, left=None, right=None):
            self._element = element
            self._parent = parent
            self._left = left
            self._right = right

    # Objects to represent position of a node.
    class Position(BinaryTree.Position):
        """An abstraction representing the location of a single tree element."""

        def __init__(self, container, node):
            """Constructor should not be invoked by user! Only for internal use."""
            self._container = container
            self._node = node

        def element(self):
            """Return the element stored at specified position."""
            return self._node._element

        def __eq__(self, other):
            """Return True if 'other' is a Position representing the same location."""
            return (type(other) is type(self)) and (other._node is self._node)

    # ----- All utility methods. ----- #

    # Given a position, this will return the associated node.
    def _validate(self, p):
        """Return node at position 'p', or raise error if position is invalid."""

        if not isinstance(p, self.Position):
            raise TypeError("Given parameter must be of type Position.")

        if p._container is not self:
            raise ValueError("Given position parameter does not belong to this container.")

        if p._node._parent is p._node:  # Convention for deprecated nodes???
            raise ValueError("Given position is no longer valid.")

        return p._node

    # Given a node, this will return its associated position.
    def _make_position(self, node):
        """Return node's Position instance, or None if node is a sentinel."""

        if node is None:
            return None
        return self.Position(self, node)

    # ----- Binary tree constructor ----- #

    def __init__(self):
        """Initialize an empty binary tree."""
        self._root = None
        self._size = 0

    # ----- Accessor Methods ----- #

    def __len__(self):
        """Return number of nodes in the tree."""
        return self._size

    def root(self):
        """Return position of root node, or None if tree is empty."""
        if self._size == 0:
            return None
        return self._make_position(self._root)

    def parent(self, p):
        """Return the position of the parent of node 'p', or None if 'p' is the root node."""
        node = self._validate(p)
        return self._make_position(node._parent)

    def num_children(self, p):
        pass

    def left(self, p):
        pass

    def right(self, p):
        pass





