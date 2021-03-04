"""This is an implementation of a deque using a doubly linked list as the underlying structure.

Created By: AJ Singh
Date: March 4, 2021
"""

from doubly_linked_list_base_class import _DoublyLinkedBase
from Stacks.implementation_using_array import Empty


class LinkedDeque(_DoublyLinkedBase):
    """An implementation of a deque ADT, using a doubly linked list."""

    def first(self):
        """Return (but do not remove) the first element in the deque."""
        if self.is_empty():
            raise Empty("No elements in deque.")
        return self._header._next._element

    def last(self):
        """Return (but do not remove) last element of the deque."""
        if self.is_empty():
            raise Empty("No elements in deque.")
        return self._trailer._prev._element

    def insert_first(self, e):
        """Insert element 'e' into the front of the deque."""
        self._insert_between(e, self._header, self._header._next)

    def insert_last(self, e):
        """Insert element 'e' into the back of the deque."""
        self._insert_between(e, self._trailer._prev, self._trailer)

    def delete_first(self):
        """Remove and return the first element in the deque."""
        if self.is_empty():
            raise Empty("No elements in deque.")
        return self._delete_node(self._header._next)

    def delete_last(self):
        """Remove and return the last element in the deque."""
        if self.is_empty():
            raise Empty("No elements in deque.")
        return self._delete_node(self._trailer._prev)
