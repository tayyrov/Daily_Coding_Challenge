"""
Question Source:Leetcode
Level: Medium
Topic: DP
Solver: Tayyrov
Date: 23.05.2022
"""
from typing import List

def findMaxForm(strs: List[str], m: int, n: int) -> int:
    dp = [[0] * (n + 1) for _ in range(m + 1)]

    for s in strs:
        zero, one = s.count("0"), s.count("1")

        for i in range(m, -1, -1):
            for j in range(n, -1, -1):
                if i >= zero and j >= one:
                    dp[i][j] = max(dp[i - zero][j - one] + 1, dp[i][j])

    return dp[m][n]
