"""An implementation of the bucket-sort algorithm.

Entries of the input sequence are integers, and we use the indices as the keys.

Created By: AJ Singh
Date: March 28, 2021
"""

from math import floor


def bucket_sort(s, k):
    """Sort a sequence 's' in non-decreasing order using the bucket-sort algorithm"""

    b = [[] for _ in range(k)]  # Setting up k empty buckets.
    m = max(s) + 1

    for i in range(len(s)):
        index = floor(k * s[i] / m)
        b[index].append(s[i])

    for i in range(k):
        b[i].sort()  # Can use any sorting algorithm for individual buckets.

    return [b[i][j] for i in range(k) for j in range(len(b[i]))]


if __name__ == "__main__":
    seq = [29, 25, 4, 49, 9, 37, 21, 43]
    print("Original:")
    print(*seq, sep=" ")

    print("\nSorted:")
    print(bucket_sort(seq, 5))
