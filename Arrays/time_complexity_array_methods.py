"""This module investigates the time complexity of various array/list methods.

Some of the code is taken from the 'evaluate_append_operation.py' module.

Created By: AJ Singh
Date: Feb 18, 2021
"""

from time import time
from tabulate import tabulate

from Arrays.dynamic_array_implementation import DynamicArray
# print(dir(DynamicArray)


def compute_average_append(n):
    """Performs n append operations to an empty list, and returns the *average* time taken."""

    data = DynamicArray()
    start = time()

    for k in range(n):
        data.append(None)
    end = time()

    return (end - start) / n


def compute_average_insert(n, index):
    """Performs n append operations to an empty list, and returns the *average* time taken."""

    data = DynamicArray()
    start = time()

    for k in range(n):
        data.insert(index, None)
    end = time()

    return (end - start) / n


if __name__ == "__main__":

    MAX_SIZE = 4
    SIZES = [f"10^{i}" for i in range(2, MAX_SIZE + 1)]
    ARRAY_SIZES = [10**i for i in range(2, MAX_SIZE+1)]

    times_taken_append = [compute_average_append(n)*(10**6) for n in ARRAY_SIZES]
    print(tabulate(zip(SIZES, times_taken_append), ["Size", "Time"]))

    print("\n\n")

    times_taken_insert = [compute_average_insert(n, index=0)*(10**6) for n in ARRAY_SIZES]
    print(tabulate(zip(SIZES, times_taken_insert), ["Size", "Time"]))
