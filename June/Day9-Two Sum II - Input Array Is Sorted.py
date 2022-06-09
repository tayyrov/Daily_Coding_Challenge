"""
Question Source:Leetcode
Level: Medium
Topic: Two pointers
Solver: Tayyrov
Date: 09.06.2022
"""
from typing import List


def twoSum(numbers: List[int], target: int) -> List[int]:
    left = 0
    right = len(numbers) - 1

    while left < right:
        curr = numbers[left] + numbers[right]
        if curr == target:
            return [left + 1, right + 1]
        if curr > target:
            right -= 1
        else:
            left += 1