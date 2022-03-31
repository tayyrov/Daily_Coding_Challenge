"""
Question Source:Leetcode
Level: Hard
Topic: Binary search
Solver: Tayyrov
Date: 31.03.2022
"""
from typing import List


def splitArray(nums: List[int], m: int) -> int:
    def can_split(capacity: int) -> bool:
        curr = 0
        needed = 1
        for n in nums:
            if curr + n > capacity:
                needed += 1
                curr = 0
            curr += n

        return needed <= m

    left = max(nums)
    right = sum(nums)

    while left <= right:
        curr_capacity = left + (right - left) // 2
        if can_split(curr_capacity):
            right = curr_capacity - 1
        else:
            left = curr_capacity + 1
    return right + 1