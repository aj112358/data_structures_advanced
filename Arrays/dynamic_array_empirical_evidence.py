"""This is just some quick code that shows how the Python 'list' class does indeed use dynamic arrays.

NOTE: For a list, 'getsizeof' only computes the number of bytes that are allocated for the size of an array, NOT the
actual data that may be stored in the array (in any case, we store our array with instances of 'None').

Created By: AJ Singh
Date: Feb 16, 2021
"""


from sys import getsizeof
from tabulate import tabulate

data = []
table = []
n = 50
for k in range(n):
    a = len(data)
    b = getsizeof(data)

    table.append([a, b])
    data.append(None)

print()
print(tabulate(table, ["Length", "Size (bytes)"]))
