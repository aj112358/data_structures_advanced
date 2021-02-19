"""This is some quick code to measure the speed of performing large number of append operations, taken from book.

Created By: AJ Singh
Date: Feb 16, 2021
"""

from time import time
from tabulate import tabulate


def compute_average(n):
    """Performs n append operations to an empty list, and returns the *average* time taken."""

    data = []
    start = time()

    for k in range(n):
        data.append(None)
    end = time()

    return (end - start) / n


if __name__ == "__main__":

    MAX_SIZE = 9
    SIZES = [f"10^{i}" for i in range(2, MAX_SIZE + 1)]

    array_sizes = [10**i for i in range(2, MAX_SIZE+1)]
    times_taken = [compute_average(n)*(10**6) for n in array_sizes]

    print(tabulate(zip(size, times_taken), ["Size", "Time"]))
