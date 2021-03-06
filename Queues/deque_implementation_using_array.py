"""An implementation of a deque with an array as the underlying structure, resizing when needed.

Most of the code is reused from the queue implementation, with a few added deque methods.

Created By: AJ Singh
Date: Feb 24, 2021
"""


class Empty(Exception):
    """The error to raise when attempting to access an element from an empty deque."""
    pass


class ArrayDeque:
    """An implementation of a deque using arrays."""

    def __init__(self, n=10):
        """Instantiating a new deque, with default size 10."""

        self._data = [None] * n  # List instance to store the deque elements.
        self._size = 0           # Actual number of elements in the deque.
        self._front = 0          # Index of the 'first' deque element.

    def __len__(self):
        """Return the actual number of elements in the deque."""
        return self._size

    def is_empty(self):
        """Return True if the deque contains no elements."""
        return self._size == 0

    def first(self):
        """Returns (but does not remove) the element at the front of the deque."""
        if self.is_empty():
            raise Empty("The deque contains no elements.")
        return self._data[self._front]

    def last(self):
        """Return (but does not remove) the 'last' element in the deque."""
        if self.is_empty():
            raise Empty("The deque contains no elements.")
        back = (self._front + self._size - 1) % len(self._data)
        return self._data[back]

    def delete_first(self):
        """Removes and returns the front element of the deque."""

        if self.is_empty():
            raise Empty("The deque contains no elements.")

        elem = self._data[self._front]  # Save element for returning (before removal from deque).

        self._size -= 1
        self._data[self._front] = None  # Remove element from the deque.
        self._front = (self._front + 1) % len(self._data)

        # Shrink size of underlying array if there are few enough elements in deque.
        if self._size <= len(self._data) // 4:
            self._resize(len(self._data) // 2)

        return elem

    def delete_last(self):
        """Removes and returns the last element of the deque."""

        if self.is_empty():
            raise Empty("The deque contains no elements.")
        
        back = (self._front + self._size - 1) % len(self._data)
        elem = self._data[back]
        
        self._size -= 1
        self._data[back] = None

        # Shrink size of underlying array if there are few enough elements in deque.
        if self._size <= len(self._data) // 4:
            self._resize(len(self._data) // 2)
            
        return elem

    def add_last(self, e):
        """Adds element 'e' to the back of the deque."""

        # Enlarge underlying array if current deque is full.
        if self._size == len(self._data):
            self._resize(self._size * 2)

        back = (self._front + self._size) % len(self._data)
        self._data[back] = e
        self._size += 1

    def add_first(self, e):
        """Adds element 'e' to the front of the deque.

        If resizing is needed, the new element is added in the '_resize' method.
        """

        # Enlarge underlying array if current deque is full.
        if self._size == len(self._data):
            self._resize(self._size * 2, elem=e)
            self._size += 1
        else:
            self._front = (self._front - 1) % len(self._data)
            self._data[self._front] = e
            self._size += 1

    def _resize(self, capacity, elem=None):
        """Resize the underlying array to have size 'capacity'.

        @param elem: An optional parameter to pass an element, used with 'add_first' method only.
        """

        temp = [None] * capacity  # New array to store deque elements.

        for k in range(self._size):

            # Adding new 'elem' to front of deque, if _resize called from 'add_first'.
            if elem and k == 0:
                temp[0] = elem
                continue

            # Copying deque elements into new array.
            temp[k] = self._data[self._front % len(self._data)]
            self._front = (self._front + 1) % len(self._data)

        # If new 'elem' was added to front, still need to add last deque element to back of new array.
        if elem:
            temp[self._size] = self._data[self._front % len(self._data)]

        self._front = 0
        self._data = temp

    def __str__(self):
        """Prints a human-readable representation of the deque."""
        return " < ".join(str(_) for _ in self._data)


if __name__ == "__main__":
    print()

    q = ArrayDeque(n=5)
    print(q)

    q.add_last("A")
    q.add_last("B")
    print(q)
    q.add_last("C")
    q.add_last("D")
    print(q)

    q.delete_first()
    print(q)

    q.add_last("E")
    print(q)

    q.add_last("F")
    print(q)

    q.delete_first()
    print(q)

    q.add_last("G")
    q.add_last("H")
    print(q)

    q.delete_first()
    q.delete_first()
    q.delete_first()
    print(q)

    q.delete_first()
    print(q)

    q.delete_first()
    print(q)

    print('-----------------------------------')

    print()

    q2 = ArrayDeque(5)
    print(q2)

    q2.add_first("A")
    q2.add_first("B")
    q2.add_first("C")
    q2.add_first("D")
    print(q2)

    q2.delete_last()
    q2.delete_last()
    print(q2)

    q2.add_first("E")
    q2.add_first("F")
    q2.add_first("G")
    print(q2)

    print(q2.last())
    print(q2.first())
    print()

    q2.add_first("H")
    print(q2)

    print(q2.last())
    print(q2.first())
