"""
Question Source:Leetcode
Level: Medium
Topic: Greedy
Solver: Tayyrov
Date: 2.07.2022
"""
from typing import List


def maxArea(h: int, w: int, horizontalCuts: List[int], verticalCuts: List[int]) -> int:
    MOD = 10 ** 9 + 7
    horizontalCuts.extend([0, h])
    verticalCuts.extend([0, w])

    def get_max_dif(lst):
        lst.sort()
        best = 0

        for x, y in zip(lst[1:], lst):
            best = max(best, x - y)

        return best

    return (get_max_dif(horizontalCuts) * get_max_dif(verticalCuts)) % MOD
