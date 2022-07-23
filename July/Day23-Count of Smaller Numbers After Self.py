"""
Question Source:Leetcode
Level: Hard
Topic: Binary
Solver: Tayyrov
Date: 23.07.2022
"""
from bisect import bisect_left
from typing import List


def countSmaller(nums: List[int]) -> List[int]:
    sor = sorted(nums)
    past = []

    ans = []
    for n in nums:
        add = bisect_left(sor, n)
        remove = bisect_left(past, n)
        ans.append(add - remove)
        past.insert(remove, n)

    return ans