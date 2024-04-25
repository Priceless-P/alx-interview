#!/usr/bin/python3

"""Minimum Operations"""


def minOperations(n):
    """Calculates the fewest number of operations
    needed to result in exactly n H characters"""

    # Base cases
    if n <= 1:
        return 0
    elif n == 2:
        return 2
    else:
        while n > 2:
            if n % 3 == 0:
                return 3 + minOperations(n//3)
            elif n % 2 == 0:
                return 2 + minOperations(n//2)
            else:
                return 1 + minOperations(n - 1)
