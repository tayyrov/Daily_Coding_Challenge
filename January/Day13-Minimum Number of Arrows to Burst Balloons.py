"""
Question Source: https://leetcode.com/problems/minimum-number-of-arrows-to-burst-balloons/
Level: Medium
Topic: Greedy
Solver: Tayyrov
Date: 01.13.2022
"""
from typing import *
from math import inf


def findMinArrowShots(points: List[List[int]]) -> int:
    arrow_num = 0

    sor = sorted(points, key=lambda x: x[1])

    previous_end = -inf

    for start, end in sor:
        if start > previous_end:  # means there is no overlap so we should shut at this moment
            previous_end = end
            arrow_num += 1

    return arrow_num
