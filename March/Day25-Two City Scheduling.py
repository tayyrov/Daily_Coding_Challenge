"""
Question Source:Leetcode
Level: Medium
Topic: Greedy
Solver: Tayyrov
Date: 25.03.2022
"""
from typing import List


def twoCitySchedCost(costs: List[List[int]]) -> int:
    ans = 0

    new = [[a - b, a, b] for a, b in costs]
    new.sort()

    left = 0
    right = len(costs) - 1

    while left < right:
        ans += new[left][1]
        ans += new[right][2]
        left += 1
        right -= 1

    return ans

"""
time complexity: nlogn
space complexity: n where n is the len of costs
"""
