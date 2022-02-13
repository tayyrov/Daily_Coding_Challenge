"""
Question Source: https://leetcode.com/problems/subsets/
Level: Medium
Topic: Bitmask
Solver: Tayyrov
Date: 13.02.2022
"""

from typing import *


def subsets(nums: List[int]) -> List[List[int]]:
    ans = []
    ln = len(nums)

    for i in range(2 * ln):
        mask = bin(i)[2:].zfill(ln)
        subset = []
        for i, j in zip(mask, nums):
            if i == "0":
                subset.append(j)
        ans.append(subset)

    return ans
# solution2:
#         ans = [[]]

#         for n in nums:
#             temp = [curr + [n] for curr in ans]
#             ans.extend(temp)
#             # extend is the same as ans += temp
#         return ans
