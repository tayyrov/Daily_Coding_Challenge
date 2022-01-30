"""
Question Source: https://leetcode.com/problems/rotate-array/
Level: Medium
Topic: Array
Solver: Tayyrov
Date: 01.30.2022
"""
from typing import *


def rotate(nums: List[int], k: int) -> None:
    """
    Do not return anything, modify nums in-place instead.
    """
    k %= len(nums)
    if k != 0:
        nums[:] = nums[-k:] + nums[:len(nums) - k]

"""
Time: O(N)
Space: O(N)
"""