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

    