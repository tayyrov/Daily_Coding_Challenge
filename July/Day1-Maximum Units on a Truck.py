"""
Question Source:Leetcode
Level: Easy
Topic: Greedy
Solver: Tayyrov
Date: 1.07.2022
"""
from typing import List


def maximumUnits(boxTypes: List[List[int]], truckSize: int) -> int:
    boxTypes.sort(key=lambda x: (-x[1], x[0]))

    ans = 0
    for a, b in boxTypes:
        if a <= truckSize:
            ans += (b * a)
            truckSize -= a
        else:
            ans += truckSize * b
            break

    return ans
