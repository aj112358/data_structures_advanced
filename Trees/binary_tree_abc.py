"""This module contains the abstract class for binary trees.

Created By: AJ Singh
Date: March 10, 2021
"""

from tree_abc import Tree


class BinaryTree(Tree):
    """An abstract base class for binary trees."""

    # ----- Abstract methods, specific for binary trees. ----- #

    def left(self, p):
        """Return position of left child node of 'p', or None if 'p' has no left child."""

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
