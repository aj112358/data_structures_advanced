"""An implementation of the bucket-sort algorithm.

Entries of the input sequence are key-value pairs.

Created By: AJ Singh
Date: March 28, 2021
"""

from math import floor


def bucket_sort(s, k):
    """Sort a sequence 's' in non-decreasing order using the bucket-sort algorithmm"""

    b = [[] for _ in range(k)]  # Setting up k empty buckets.
    # m = len(s) - 1
    m = max(s)+1
    for i in range(len(s)):
        x = floor(k * s[i] / m)
        print(x)
        b[floor(k * s[i] / m)].append(s[i])

    for i in range(k):
        b[i].sort()

    return b


if __name__ == "__main__":
    seq = [29, 25, 3, 49, 9, 37, 21, 43]



    print(bucket_sort(seq, 5))
