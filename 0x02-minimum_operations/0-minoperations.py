#!/usr/bin/python3

"""Minimum Operations"""


def minOperations(n):
    """Calculates the fewest number of operations
    needed to result in exactly n H characters"""

    # Base cases
    if n <= 1:
        return 0

    operations = 0
    divisor = 2  # Start with 2 as the divisor

    while n > 1:
        # Check if n is divisible by the current divisor
        if n % divisor == 0:
            n //= divisor  # Perform the division
            operations += divisor  # Increment the number of operations
        else:
            # If not divisible, increment the divisor
            divisor += 1

    return operations
