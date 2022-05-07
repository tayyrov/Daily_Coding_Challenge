"""
Question Source:Leetcode
Level: Medium
Topic: Stack
Solver: Tayyrov
Date: 07.05.2022
"""

from math import inf
from typing import List


def find132pattern(nums: List[int]) -> bool:
    stack = []
    curMin = inf
    for n in nums:

        while stack and stack[-1][0] <= n:
            stack.pop()

        if stack and stack[-1][1] < n < stack[-1][0]:
            return True

        stack.append((n, curMin))

        curMin = min(curMin, n)

    return False