#!/usr/bin/python3
"""
    This program checks the the minimum number of
    operation to get 'n' 'H'
"""


def minOperations(n):
    """
    This function uses prime factors to get the minimum number of operations
    for 'n' 'H'
    n: int
    """
    if not (isinstance(n, int) and n > 0):
        return (0)
    # counts number of operations
    count = 0
    # d is the prime factor, starting with 2
    d = 2
    while n > 1:
        while n % d == 0:
            count += d
            n = n / d
        d += 1
    return count
