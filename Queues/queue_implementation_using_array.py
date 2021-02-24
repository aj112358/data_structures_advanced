"""An implementation of a queue with an array as the underlying structure, resizing when needed.

Created By: AJ Singh
Date: Feb 23, 2021
"""


class Empty(Exception):
    """The error to raise when attempting to access an element from an empty stack."""
    pass


class ArrayQueue:
    """An implementation of a queue following the FIFO principle using arrays."""

    def __init__(self, n=10):
        """Instantiating a new queue, with default size 10."""

        self._data = [None] * n  # List instance to store the queue elements.
        self._size = 0           # Actual number of elements in the queue.
        self._front = 0          # Index of the 'first' queue element.

    def __len__(self):
        """Return the actual number of elements in the queue."""
        return self._size

    def is_empty(self):
        """Return True if the queue contains no elements."""
        return self._size == 0

    def first(self):
        """Returns (but does not remove) the element at the front of the queue."""
        if self.is_empty():
            raise Empty("The queue contains no elements.")
        return self._data[self._front]

    def dequeue(self):
        """Removes and returns the front element of the queue."""

        if self.is_empty():
            raise Empty("The queue contains no elements.")

        elem = self._data[self._front]  # Save element for returning (before removal from queue).

        self._size -= 1
        self._data[self._front] = None  # Remove element from the queue.
        self._front = (self._front + 1) % len(self._data)

        # Shrink size of underlying array if there are few enough elements in queue.
        if self._size <= len(self._data) // 4:
            self._resize(len(self._data) // 2)

        return elem

    def enqueue(self, e):
        """Adds element 'e' to the back of the queue."""

        # Enlarge underlying array if current queue is full.
        if self._size == len(self._data):
            self._resize(self._size * 2)

        back = (self._front + self._size) % len(self._data)
        self._data[back] = e
        self._size += 1

    def _resize(self, capacity):
        """Resize the underlying array to have size 'capacity'."""

        temp = [None] * capacity  # New array to store queue elements.

        for k in range(self._size):
            temp[k] = self._data[self._front % len(self._data)]  # Copy queue elements into new array.
            self._front = (self._front + 1) % len(self._data)

        self._front = 0
        self._data = temp

    def __str__(self):
        """Prints a human-readable representation of the queue."""
        return " < ".join(str(_) for _ in self._data)


if __name__ == "__main__":
    print()

    q = ArrayQueue(n=5)

    q.enqueue("A")
    q.enqueue("B")
    q.enqueue("C")
    q.enqueue("D")
    print(q)

    q.dequeue()
    print(q)

    q.enqueue("E")
    print(q)

    q.enqueue("F")
    print(q)

    q.dequeue()
    print(q)

    q.enqueue("G")
    q.enqueue("H")
    print(q)

    q.dequeue()
    q.dequeue()
    q.dequeue()
    print(q)

    q.dequeue()
    print(q)

    q.dequeue()
    print(q)
