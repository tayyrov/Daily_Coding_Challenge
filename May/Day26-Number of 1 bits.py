"""
Question Source:Leetcode
Level: Easy
Topic: Bit Manipulation
Solver: Tayyrov
Date: 26.05.2022
"""
def hammingWeight(n: int) -> int:

    ct = 0

    while n > 0:
        if n & 1 > 0:
            ct += 1
        n = n >> 1

    return ct