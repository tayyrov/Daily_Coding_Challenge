"""
Question Source:Leetcode
Level: Easy
Topic: DP
Solver: Tayyrov
Date: 10.07.2022
"""
from typing import List


def minCostClimbingStairs(cost: List[int]) -> int:
    ln = len(cost)
    dp = [0] * ln
    for i in range(ln):
        if i < 2:
            dp[i] = cost[i]
        else:
            dp[i] = cost[i] + min(dp[(i - 2):i])
    print(dp)
    return min(dp[-2:])