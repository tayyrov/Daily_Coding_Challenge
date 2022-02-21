"""
Question Source: https://leetcode.com/problems/majority-element/
Level: Easy
Topic: Counting
Solver: Tayyrov
Date: 21.02.2022
"""

from typing import List


def majorityElement(nums: List[int]) -> int:
    ln = len(nums)
    x = nums[0]
    cnt = 1

    for i in range(1, ln):
        if nums[i] == x:
            cnt += 1
        else:
            cnt -= 1

        if cnt == 0:
            x = nums[i]
            cnt = 1

    return x


"""
Time: O(N)
Space: O(1)
"""
