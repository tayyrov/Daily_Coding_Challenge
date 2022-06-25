"""
Question Source:Leetcode
Level: Medium
Topic: greedy
Solver: Tayyrov
Date: 25.06.2022
"""
from math import inf
from typing import List


def checkPossibility(nums: List[int]) -> bool:
    nums = [-inf] + nums + [inf]

    def is_sorted(l):
        return l == sorted(l)

    ln = len(nums)

    for i in range(1, ln - 1):
        if nums[i - 1] > nums[i]:
            lst1 = nums[::]
            lst1[i - 1] = nums[i]
            nums[i] = nums[i + 1]
            return is_sorted(nums) or is_sorted(lst1)

    return True
