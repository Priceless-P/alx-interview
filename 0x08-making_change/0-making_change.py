#!/usr/bin/python3
"""Change comes from within
"""


def makeChange(coins, total):
    """Given a pile of coins of different values,
    determine the fewest number of coins needed
    to meet a given amount total
    """
    if total <= 0:
        return 0
    new = [float('inf')] * (total + 1)
    new[0] = 0

    for coin in coins:
        for i in range(coin, total + 1):
            new[i] = min(new[i], new[i - coin] + 1)
    return new[total] if new[total] != float('inf') else -1
