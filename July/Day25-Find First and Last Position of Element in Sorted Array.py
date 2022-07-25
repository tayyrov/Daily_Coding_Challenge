"""
Question Source:Leetcode
Level: Medium
Topic: Binary
Solver: Tayyrov
Date: 25.07.2022
"""
from typing import List


def searchRange(nums: List[int], target: int) -> List[int]:
    left = 0
    right = len(nums) - 1
    ans = [-1, -1]
    found = False
    while left <= right:
        mid = left + (right - left) // 2
        num = nums[mid]
        if num == target:
            left = mid + 1
            found = True
        elif num < target:
            left = mid + 1
        else:
            right = mid - 1
    if not found:
        return ans
    ans[1] = left - 1

    left = 0
    right = len(nums) - 1
    while left <= right:
        mid = left + (right - left) // 2
        num = nums[mid]
        if num == target:
            right = mid - 1
        elif num < target:
            left = mid + 1
        else:
            right = mid - 1
    ans[0] = right + 1
    return ans