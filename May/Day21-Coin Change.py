"""
Question Source:Leetcode
Level: Medium
Topic: DP
Solver: Tayyrov
Date: 21.05.2022
"""
from math import inf
from typing import List


def coinChange(coins: List[int], amount: int) -> int:
    dp = [0] + [inf] * amount
    for a in range(1, amount + 1):
        for c in coins:
            if a - c >= 0:
                dp[a] = min(dp[a], dp[a - c] + 1)

    ans = dp[-1]

    return ans if ans != inf else -1