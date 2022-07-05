"""
Question Source:Leetcode
Level: Medium
Topic: Greedy
Solver: Tayyrov
Date: 5.07.2022
"""

from typing import List


def longestConsecutive(nums: List[int]) -> int:
    all_set = set(nums)
    best = 0
    for n in nums:
        if n-1 not in all_set:
            temp = 0
            while n in all_set:
                n += 1
                temp += 1
            best = max(best, temp)

    return best
