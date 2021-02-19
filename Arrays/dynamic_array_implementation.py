"""This is a manual implementation of a dynamic array, for pedagogical purposes.

Created By: AJ Singh
Date: Feb 16, 2021
"""

import ctypes


class DynamicArray:
    """A dynamic array class similar to a Python list."""

    def __init__(self):
        """Creates an empty array of default capacity one."""

        self._n = 0                                 # Actual number of elements in the array
        self._capacity = 1
        self._A = self._make_array(self._capacity)  # Creating the low-level array using ctypes module.

    def __len__(self):
        """Return the number of elements stored in the array."""
        return self._n

    def __getitem__(self, k):
        """Return element at index k."""

        if not 0 <= k < self._n:
            raise IndexError("Invalid index.")
        return self._A[k]

    def append(self, obj):
        """Add an object to the end of the array."""

        # Check if re-sizing is needed (if current array is full; new array is double in size).
        if self._n == self._capacity:
            self._resize(2 * self._capacity)

        self._A[self._n] = obj  # Appending object to the end of the array.
        self._n += 1

    def _make_array(self, c):
        """Return a new array with capacity c."""
        return (c * ctypes.py_object)()

    def _resize(self, c):
        """Resize the internal array, _A, to capacity c."""

        B = self._make_array(c)     # Making new low-level array of capacity c.
        for k in range(self._n):
            B[k] = self._A[k]       # Copying current elements into new array.

        self._A = B                 # Changing original identifier to reference new larger array.
        self._capacity = c          # Updating new capacity.

    def insert(self, k, value):
        """Insert 'value' at index k, shifting subsequent values rightward in the list.

        For simplicity, we assume that 0 <= k <= n.
        """

        # Check if resizing is needed.
        if self._n == self._capacity:
            self._resize(2 * self._capacity)

        # Shift values rightward, from index k and onward. Do the shifting from the end of the array going backwards.
        for j in range(self._n, k, -1):
            self._A[j] = self._A[j-1]

        self._A[k] = value  # Assign 'value' to index k.
        self._n += 1        # Increment number of actual elements in list.

    def remove(self, value):
        """Remove the first occurrence of 'value' from the list.

        For simplicity, we do not consider re-sizing via shrinking of the underlying array.
        """

        # Iterate through array to look for 'value'.
        for k in range(self._n):

            # If 'value' is found (at index k).
            if self._A[k] == value:

                # Shift values leftward, starting from the front (index k).
                for j in range(k, self._n - 1):
                    self._A[j] = self._A[j+1]

                self._A[self._n - 1] = None  # Set last element to 'None'.
                self._n -= 1                 # Update actual number of elements.

                return  # Exit the remove method.

        raise ValueError("Value not found.")


if __name__ == "__main__":
    print("Hello world")
