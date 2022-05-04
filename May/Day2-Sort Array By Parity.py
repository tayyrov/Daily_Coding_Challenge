"""
Question Source:Leetcode
Level: Easy
Topic: Stack
Solver: Tayyrov
Date: 02.05.2022
"""
from typing import List


def sortArrayByParity(nums: List[int]) -> List[int]:
    left = 0
    right = len(nums) - 1

    while left < right:
        while left < right and nums[left] % 2 == 0:
            left += 1
        while -1 < right and nums[right] % 2:
            right -= 1
        if left < right:
            nums[left], nums[right] = nums[right], nums[left]
        left += 1
        right -= 1

    return nums
