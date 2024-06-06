#!/usr/bin/python3
"""Change comes from within
"""


def makeChange(coins, total):
    """Given a pile of coins of different values,
    determine the fewest number of coins needed
    to meet a given amount total using a greedy approach.
    """
    if total <= 0:
        return 0

    # Sort the coins in descending order
    coins.sort(reverse=True)

    num_coins = 0
    remaining_total = total

    for coin in coins:
        if remaining_total <= 0:
            break

        count = remaining_total // coin
        num_coins += count
        remaining_total -= coin * count

    if remaining_total > 0:
        return -1

    return num_coins
