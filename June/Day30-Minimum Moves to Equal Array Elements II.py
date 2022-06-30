"""
Question Source:Leetcode
Level: Medium
Topic: Greedy
Solver: Tayyrov
Date: 30.06.2022
"""
from typing import List


def minMoves2(nums: List[int]) -> int:
    nums.sort()
    len_nums = len(nums)

    middle = nums[len_nums // 2]

    ans = 0
    for n in nums:
        ans += abs(middle - n)

    return ans

"""
Time: nlogn
Space: O(1)
"""