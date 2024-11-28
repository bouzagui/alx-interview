#!/usr/bin/python3
"""making change"""


def makeChange(coins, total):
    """
    Determine the fewest number of coins needed to meet a given amount total.
    Args:
        coins (list): List of the values of the coins in your possession.
        total (int): The total amount to achieve using the fewest coins.
    Returns:
        int: Fewest number of coins needed to meet the total, or
        -1 if not possible.
    """
    if total <= 0:
        return 0
    coins.sort(reverse=True)

    count = 0
    for coin in coins:
        if total <= 0:
            break
        count += total // coin
        total %= coin

    if total != 0:
        return -1

    return count
