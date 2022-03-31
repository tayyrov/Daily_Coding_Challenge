"""
Question Source:Leetcode
Level: Medium
Topic: Array
Solver: Tayyrov
Date: 03.03.2022
"""
from typing import List
from itertools import groupby


def numberOfArithmeticSlices(nums: List[int]) -> int:
    # 4 3 2 1
    """
    total = n*(n+1)//2
    substract = -ln - (ln-1)

    """

    difs = []

    ln = len(nums)

    for i in range(1, ln):
        difs.append(nums[i] - nums[i - 1])
    ans = 0
    for _, grp in groupby(difs):
        ln = len(list(grp)) + 1

        if ln >= 3:
            temp = ln * (ln + 1) // 2
            temp -= (ln + ln - 1)
            ans += temp

    return ans
