"""
Question Source:Leetcode
Level: Easy
Topic: Prefix Sum
Solver: Tayyrov
Date: 01.06.2022
"""
from typing import List

def runningSum(nums: List[int]) -> List[int]:
    ln = len(nums)

    ans = [nums[0]]

    for i in range(1, ln):
        ans.append(ans[i - 1] + nums[i])

    return ans
    # 2nd solution
    # return list(accumulate(nums))
