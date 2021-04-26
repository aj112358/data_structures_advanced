"""This is the base class for all our future realizations of a priority queue.

It uses the composition design pattern to store key-value pairs as a single object.
Created By: AJ Singh
Date: April 25, 2021
"""


class PriorityQueueBase:
    """ABC for a priority queue."""

    class _Item:
        """Lightweight composite to store priority queue items."""

        __slots__ = "_key", "_value"

        def __init__(self, k, v):
            self._key = k
            self._value = v

        def __lt__(self, other):
            return self._key < other._key

    def is_empty(self):  # Based on an abstract __len__ method.
        """Returns True if priority queue contains no elements."""
        return len(self) == 0
