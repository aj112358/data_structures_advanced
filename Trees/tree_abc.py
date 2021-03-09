"""This module contains the ABC for a tree structure.

Created By: AJ Singh
Date: March 9, 2021
"""

from abc import abstractmethod

class Tree:
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

    