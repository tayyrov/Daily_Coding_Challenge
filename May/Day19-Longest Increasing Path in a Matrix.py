"""
Question Source:Leetcode
Level: Hard
Topic: DFS
Solver: Tayyrov
Date: 19.05.2022
"""
from typing import List


def longestIncreasingPath(matrix: List[List[int]]) -> int:
    rows = len(matrix)
    cols = len(matrix[0])

    dp = [[-1] * cols for _ in range(rows)]

    def is_valid(r, c):
        return 0 <= r < rows and 0 <= c < cols

    def dfs(i, j, prev):

        if not is_valid(i, j) or matrix[i][j] <= prev:
            return 0

        if dp[i][j] != -1:
            return dp[i][j]

        left = dfs(i, j - 1, matrix[i][j])
        right = dfs(i, j + 1, matrix[i][j])
        top = dfs(i - 1, j, matrix[i][j])
        bottom = dfs(i + 1, j, matrix[i][j])

        dp[i][j] = max(left, right, top, bottom) + 1

        return dp[i][j]

    ans = -1

    for r in range(rows):
        for c in range(cols):
            ans = max(ans, dfs(r, c, -1))

    return ans