"""A module that defines a binary tree using a linked structure, adapted from book.

Created By: AJ Singh
Date: March 11, 2021
"""

from binary_tree_abc import BinaryTree


class LinkedBinaryTree(BinaryTree):
    """A binary tree structure using a linked representation."""

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