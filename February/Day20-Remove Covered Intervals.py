"""
Question Source: https://leetcode.com/problems/remove-covered-intervals/
Level: Medium
Topic: Stack
Solver: Tayyrov
Date: 20.02.2022
"""
from typing import List


def removeCoveredIntervals(self, intervals: List[List[int]]) -> int:
    intervals.sort()

    stack = []
    ans = 0
    for a, b in intervals:
        if stack and stack[1] >= b:
            continue
        elif stack and stack[0] == a:
            stack[1] = b
        else:
            stack = [a, b]
            ans += 1

    return ans


"""
Time: O(NLogN)
Space: O(1)
"""
