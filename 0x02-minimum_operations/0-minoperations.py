#!/usr/bin/python3
"""Module to calculate the minimum number of operations needed to achieve n 'H'
 characters."""


def minOperations(n):
    """
    Calculate the minimum number of operations to achieve exactly n
    'H' characters in the file.

    The only operations allowed are "Copy All" and "Paste".
    The strategy is to find the prime factors of n, with each factor
    representing a copy-paste cycle.

    Args:
        n (int): The number of 'H' characters to achieve.

    Returns:
        int: The minimum number of operations required,
        or 0 if n is impossible.
    """

    if n <= 1:
        return 0

    operations = 0
    divisor = 2

    while n > 1:
        while n % divisor == 0:
            operations += divisor
            n //= divisor
        divisor += 1

    return operations
