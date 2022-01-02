"""
Question Source: https://leetcode.com/problems/pairs-of-songs-with-total-durations-divisible-by-60/
Level: Medium
Topic: Hash Table
Solver: Tayyrov
Date: 02.01.2022
"""
from collections import Counter


def numPairsDivisibleBy60(time) -> int:
    remainders = [num % 60 for num in time]
    frequency_table = Counter(remainders)

    # 0 and 30 are the special cases so calculate them separately
    zeros = frequency_table[0]
    total_pairs = zeros * (zeros - 1) // 2

    thirties = frequency_table[30]
    total_pairs += thirties * (thirties - 1) // 2

    for i in range(1, 30):
        total_pairs += frequency_table[60 - i] * frequency_table[i]

    return total_pairs


def check():
    assert numPairsDivisibleBy60([30, 20, 150, 100, 40]) == 3
    assert numPairsDivisibleBy60([60, 60, 60, 1, 59, 30, 30, 30, 29, 31]) == 8
    print("All run is OK")


check()
