"""This module contains the abstract class for binary trees.

Created By: AJ Singh
Date: March 10, 2021
"""

from abc import abstractmethod
from tree_abc import Tree


class BinaryTree(Tree):
    """An abstract base class for binary trees."""

    # ----- Abstract methods, specific for binary trees. ----- #

    @abstractmethod
    def left(self, p):
        """Return position of left child node of 'p', or None if 'p' has no left child."""

    @abstractmethod
    def right(self, p):
        """Return position of right child of 'p', or None if 'p' has no right child."""

    # ----- Concrete methods ----- #

    def sibling(self, p):
        """Return the position that represents the sibling of node 'p', or None if 'p' has no siblings."""
        parent = self.parent(p)
        if parent is None:  # p is the root of the tree, hence has no siblings.
            return None

        if p == self.left(parent):
            return self.right(parent)
        else:
            return self.left(parent)

        # for child in self.children(parent):
        #     if p != child:
        #         return child
        # return None

    def children(self, p):
        """Generate an iteration of the children of node 'p'."""

        if self.left(p) is not None:
            yield self.left(p)
        if self.right(p) is not None:
            yield self.right(p)

    # ----- Tree Traversal Algorithms ----- #

    # For binary trees, we use inorder traversal as the default (useful in applications).
    def positions(self):
        """Generate an iteration of a binary tree's positions, using inorder traversal."""
        return self.inorder()  # Return entire iteration as an object.

    # Utility method to help with determining subtree for inorder traversal.
    def _subtree_inorder(self, p):
        """Generate an inorder iteration of positions in subtree rooted at p."""
        if self.left(p) is not None:
            for other in self._subtree_inorder(self.left(p)):
                yield other

        yield p  # Return p in-between visits of subtrees.

        if self.right(p) is not None:
            for other in self._subtree_inorder(self.right(p)):
                yield other

    def inorder(self):
        """Generate an inorder iteration of positions in the tree."""
        if not self.is_empty():
            for p in self._subtree_inorder(self.root()):
                yield p  # Re-yielding all positions generated in the recursive process in utility method.
