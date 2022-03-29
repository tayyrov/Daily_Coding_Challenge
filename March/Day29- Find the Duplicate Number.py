"""
Question Source:Leetcode
Level: Medium
Topic: Array
Solver: Tayyrov
Date: 29.03.2022
"""
from typing import List

def findDuplicate(nums: List[int]) -> int:
    arr = [1] * len(nums)

    for n in nums:
        if arr[n] == - 1:
            return n
        arr[n] = -1

