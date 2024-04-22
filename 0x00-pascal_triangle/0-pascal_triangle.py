#!/usr/bin/python3
"""Pascals Triangle"""


def pascal_triangle(n: str):
    """Generate a Pascals triangle given a
    number of row. It returns a List of List of Integers"""
    if n <= 0:
        return []
    # Base case is [1]
    elif n == 1:
        return [[1]]
    else:
        triangle = pascal_triangle(n - 1)
        last_row = triangle[-1]
        new_row = [1]
        for i in range(1, len(last_row)):
            # Value of each number in a row is a sum of two
            # numbers right and left above it.
            new_row.append(last_row[i - 1] + last_row[i])
        new_row.append(1)
        triangle.append(new_row)
        return triangle
