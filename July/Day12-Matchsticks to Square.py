"""
Question Source:Leetcode
Level: Medium
Topic: Backtracking
Solver: Tayyrov
Date: 12.07.2022
"""
from functools import cache
from typing import List


def makesquare(m: List[int]) -> bool:
    sm = sum(m)
    ln = len(m)
    if sm % 4 != 0:
        return False

    side = sm // 4
    m.sort(reverse=True)
    if max(m) > side:
        return False

    @cache
    def solve(l1, l2, l3, l4, idx):
        nonlocal side

        if idx == ln:
            return l1 == l2 == l3 == l4
        if max(l1, l2, l3, l4) > side:
            return False
        return solve(l1 + m[idx], l2, l3, l4, idx + 1) or \
               solve(l1, l2 + m[idx], l3, l4, idx + 1) or \
               solve(l1, l2, l3 + m[idx], l4, idx + 1) or \
               solve(l1, l2, l3, l4 + m[idx], idx + 1)

    return solve(0, 0, 0, 0, 0)