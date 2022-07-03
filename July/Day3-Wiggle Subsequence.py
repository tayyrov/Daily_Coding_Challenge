"""
Question Source:Leetcode
Level: Medium
Topic: Greedy
Solver: Tayyrov
Date: 3.07.2022
"""
from typing import List


def wiggleMaxLength(nums: List[int]) -> int:
    f = 1
    r = 1
    nums_len = len(nums)

    for i in range(1, nums_len):
        if nums[i - 1] > nums[i]:
            f = r + 1
        elif nums[i - 1] < nums[i]:
            r = f + 1

    return max(f, r)

"""
Time: O(N)
Space: O(1)
"""