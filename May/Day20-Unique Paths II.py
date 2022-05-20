"""
Question Source:Leetcode
Level: Medium
Topic: DFS, DP
Solver: Tayyrov
Date: 20.05.2022
"""
from typing import List


def uniquePathsWithObstacles(o: List[List[int]]) -> int:
    m = len(o)
    n = len(o[0])

    for r in range(m):
        for c in range(n):
            if o[r][c] == 1:
                o[r][c] = 0
            else:
                if r > 0 and c > 0:
                    o[r][c] = o[r - 1][c] + o[r][c - 1]
                elif r > 0:
                    o[r][c] = o[r - 1][c]
                elif c > 0:
                    o[r][c] = o[r][c - 1]
                else:
                    o[r][c] = 1
    return o[-1][-1]