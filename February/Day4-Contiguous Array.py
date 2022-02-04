"""
Question Source: https://leetcode.com/problems/contiguous-array/
Level: Medium
Topic: Hash Table
Solver: Tayyrov
Date: 04.02.2022
"""
from typing import *
from collections import Counter


def findMaxLength(nums: List[int]) -> int:
    seen = Counter()
    seen[0] = -1
    pre_sum = 0
    max_window_size = 0
    for i, n in enumerate(nums):
        if n == 1:
            pre_sum += n
        else:
            pre_sum -= 1

        if pre_sum in seen: # mean the sum of the numbers from that first seen value till now is zero means equal 0
            # and 1
            ans = max(max_window_size, i - seen[pre_sum])
        else:  # update this for the first time only in order to get the max window size
            seen[pre_sum] = i

    return max_window_size
"""
Time: O(N)
Space: O(N)
"""