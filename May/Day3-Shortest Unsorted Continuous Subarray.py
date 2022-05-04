"""
Question Source:Leetcode
Level: Medium
Topic: Stack
Solver: Tayyrov
Date: 03.05.2022
"""
from typing import List

def findUnsortedSubarray(nums: List[int]) -> int:
    sor = sorted(nums)
    while sor and nums and (sor[-1] == nums[-1]):
        sor.pop()
        nums.pop()
    nums = nums[::-1]
    sor = sor[::-1]
    print(nums, sor)
    while sor and nums and sor[-1] == nums[-1]:
        sor.pop()
        nums.pop()

    return len(nums)
