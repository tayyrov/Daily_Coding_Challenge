"""
Question Source:Leetcode
Level: Medium
Topic: Stimulation
Solver: Tayyrov
Date: 13.04.2022
"""
from typing import List

def generateMatrix(n: int) -> List[List[int]]:
    def valid(r, c):
        return 0 <= r < n and 0 <= c < n
    ans = [[0] * n for _ in range(n)]
    r, c = 0, 0
    dr, dc = 0, 1
    for num in range(1, n ** 2 + 1):
        ans[r][c] = num
        if not valid(r + dr, c + dc) or ans[r + dr][c + dc] != 0:
            dr, dc = dc, -dr
        r += dr
        c += dc
    return ans