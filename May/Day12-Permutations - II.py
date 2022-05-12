"""
Question Source:Leetcode
Level: Medium
Topic: Backtracking
Solver: Tayyrov
Date: 12.05.2022
"""

from typing import List

def permuteUnique(nums: List[int]) -> List[List[int]]:
    def permute(nums):
        if len(nums) == 0:
            return []
        if len(nums) == 1:
            return [nums]
        ans = []
        for i in range(len(nums)):
            curr = nums[i]
            rem = nums[:i] + nums[i + 1:]

            for p in permute(rem):
                ans.append([curr] + p)
        return ans

    ans = set(tuple(lst) for lst in permute(nums))
    return [list(t) for t in ans]