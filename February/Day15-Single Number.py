"""
Question Source: https://leetcode.com/problems/single-number/
Level: Easy
Topic: Bitmask
Solver: Tayyrov
Date: 15.02.2022
"""
from typing import *


def singleNumber(self, nums: List[int]) -> int:
    ans = 0
    for i in nums:
        ans ^= i

    return ans

"""
Time: O(N)
Space: O(1)
"""
