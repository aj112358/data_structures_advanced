"""This module contains the ABC for a tree structure.

Created By: AJ Singh
Date: March 9, 2021
"""

from abc import abstractmethod, ABC


class Tree(ABC):
    """An ABC for tree structures."""

    # Objects to represent position of a tree node.
    class Position:
        """An abstraction representing the location of a single tree element."""

        @abstractmethod
        def element(self):
            """Return the element stored at specified position."""

        @abstractmethod
        def __eq__(self, other):
            """Return True if 'other' is a Position representing the same location."""

        def __ne__(self, other):
            """Return True if 'other' does not represent the same location."""
            return not (self == other)

    # ----- Abstract methods. ----- #

    @abstractmethod
    def root(self):
        """Return position corresponding to the root of the tree, or None if tree is empty."""

    @abstractmethod
    def parent(self, p):
        """Return position corresponding to the parent of node 'p', or None if 'p' is the root."""

    @abstractmethod
    def num_children(self, p):
        """Return the number of child nodes associated with node 'p'."""

    @abstractmethod
    def children(self, p):
        """Generate an iteration of the children of node 'p'."""

    @abstractmethod
    def __len__(self):
        """Return the total number of nodes in the tree."""

    # ----- Concrete methods supported for all subclasses. ----- #

    def is_root(self, p):
        """Return True if position 'p' is the root of the tree, else return False."""
        return p == self.root()

    def is_leaf(self, p):
        """Return True if position 'p' does *not* have any children."""
        return self.num_children(p) == 0

    def is_empty(self):
        """Return True if the tree is empty."""
        return len(self) == 0

    # ----- Other useful concrete methods (apart from ADT). ----- #

    def depth(self, p):
        """Return the number of levels separating the node at 'p' from the root.

        Essentially, the number of ancestors of 'p', excluding 'p' itself.
        """

        if self.is_root(p):
            return 0
        else:
            return 1 + self.depth(self.parent(p))

    # Non-public method to assist in computing height.
    def __height(self, p):
        """Return height of sub-tree rooted at 'p'."""
        if self.is_leaf(p):
            return 0
        else:
            return 1 + max(self.__height(c) for c in self.children(p))

    # Concrete method for computing height.
    def height(self, p=None):
        """Return height of the sub-tree rooted at 'p'.

        If 'p' is None, then return the height of entire tree.
        """
        if p is None:
            p = self.root()
        return self.__height(p)

    # ----- Tree Traversal Algorithms ----- #

    def __iter__(self):
        """Generate an iteration of the *elements* of a tree."""
        for p in self.positions():
            yield p.element()

    # By default, uses preorder traversal to get the positions.
    def positions(self):
        """Generate an iteration of the tree's positions."""
        return self.preorder()  # Return entire iteration as an object.

    # Utility method to help with determining subtree for preorder traversal.
    def _subtree_preorder(self, p):
        """Generate a preorder iteration of positions in subtree rooted at p."""
        yield p  # Visit p *before* visiting its subtrees.
        for c in self.children(p):
            for other in self._subtree_preorder(c):  # Do preorder for subtree of c.
                yield other

    def preorder(self):
        """Generate a preorder iteration of positions in the tree."""
        if not self.is_empty():
            for p in self._subtree_preorder(self.root()):
                yield p  # Re-yielding all positions generated in the recursive process in utility method.

    # Utility method to help with determining subtree for postorder traversal.
    def _subtree_postorder(self, p):
        """Generate a postorder iteration of positions in subtree rooted at p."""
        for c in self.children(p):
            for other in self._subtree_postorder(c):  # Do preorder for subtree of c.
                yield other
        yield p# Visit p *after* visiting its subtrees.

    def postorder(self):
        """Generate a postorder iteration of positions in the tree."""
        if not self.is_empty():
            for p in self._subtree_postorder(self.root()):
                yield p  # Re-yielding all positions generated in the recursive process in utility method.
