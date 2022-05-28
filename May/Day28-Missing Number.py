"""
Question Source:Leetcode
Level: Easy
Topic: Math
Solver: Tayyrov
Date: 28.05.2022
"""
from typing import List

def missingNumber(nums: List[int]) -> int:
    ln = len(nums)

    return ln * (ln + 1) // 2 - sum(nums)