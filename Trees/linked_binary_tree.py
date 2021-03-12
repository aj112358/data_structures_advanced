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
        """Return the number of children at position 'p'."""
        node = self._validate(p)
        count = 0
        if node._left:
            count += 1
        if node._right:
            count += 1
        return count

    def left(self, p):
        """Return the position of p's left child, or None if it has no left child."""
        node = self._validate(p)
        return self._make_position(node._left)

    def right(self, p):
        """Return the position of p's right child, or None if it has no right child."""
        node = self._validate(p)
        return self._make_position(node._right)

    # ----- Update Methods (all are non-public) ----- #

    def _add_root(self, e):
        """Create a root node containing element 'e' for an empty tree, and return the new position."""

        if self._root is not None:
            raise ValueError("Root node already exists for this tree.")

        new_root = self._Node(element=e)
        self._root = new_root
        self._size += 1
        return self._make_position(self._root)

    def _add_left(self, p, e):
        """Create a new left child for node at position 'p' containing element 'e'.

        Raise ValueError if position is invalid, or if position already has left child.
        @return - position of the newly added left child node
        """
        parent_node = self._validate(p)
        if parent_node._left is not None:
            raise ValueError("Node already has a left child.")

        new_left = self._Node(element=e, parent=parent_node)
        parent_node._left = new_left
        self._size += 1
        return self._make_position(parent_node._left)

    def _add_right(self, p, e):
        """Create a new right child for node at position 'p' containing element 'e'.

        Raise ValueError if position is invalid, or if position already has right child.
        @return - position of the newly added right child node
        """
        parent_node = self._validate(p)
        if parent_node._right is not None:
            raise ValueError("Node already has a right child.")

        new_right = self._Node(element=e, parent=parent_node)
        parent_node._right = new_right
        self._size += 1
        return self._make_position(parent_node._right)

    def _replace(self, p, e):
        """Replace the element at position 'p' with new element 'e', and return the old element."""
        node = self._validate(p)
        elem = node._element
        node._element = e
        return elem

    def _delete(self, p):
        """Remove the node at position 'p' and replace it with its child (if any).

        Raise ValueError if position 'p' has two child nodes (ambiguity), or is invalid.
        @return - element that was stored
        """

        if self.num_children(p) == 2:
            raise ValueError("Node at p has two children.")

        node = self._validate(p)
        elem = node._element
        child = node._left if node._left else node._right  # Possible to have no child nodes, hence None.
        parent = node._parent

        if child is not None:
            child._parent = parent

        if parent is None:  # Node to delete IS the root node.
            self._root = child

        if parent is not None:  # Node to delete is NOT the root node.
            if node == parent._left:
                parent._left = child
            if node == parent._right:
                parent._right = child

        node._parent = node  # Convention for deprecated node???
        self._size -= 1
        return elem

    def _attach(self, p, t1, t2):
        pass

