"""
Question Source:Leetcode
Level: Easy
Topic: Binary Search
Solver: Tayyrov
Date: 26.03.2022
"""

from typing import List


def search(nums: List[int], target: int) -> int:
    left = 0
    right = len(nums) - 1

    while left <= right:
        middle = left + (right - left) // 2

        if nums[middle] > target:
            right = middle - 1
        elif nums[middle] < target:
            left = middle + 1
        else:
            return middle

    return -1
