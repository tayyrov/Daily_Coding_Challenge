"""
Question Source:Leetcode
Level: Medium
Topic: Two pointers
Solver: Tayyrov
Date: 11.06.2022
"""
from typing import List


def minOperations(nums: List[int], x: int) -> int:
    total = sum(nums)

    rem = total - x

    if rem < 0:
        return -1

    left = 0
    presum = 0
    ans = -1
    for right, number in enumerate(nums):
        presum += number

        while presum > rem:
            presum -= nums[left]
            left += 1

        if presum == rem:
            ans = max(ans, right - left + 1)

    return ans if ans == -1 else len(nums) - ans

"""
Time: O(N)
Space: O(1)
"""