"""
Question Source:Leetcode
Level: Hard
Topic: DP
Solver: Tayyrov
Date: 18.07.2022
"""
from collections import defaultdict
from typing import List


def numSubmatrixSumTarget(matrix: List[List[int]], target: int) -> int:
    rows = len(matrix)
    cols = len(matrix[0])
    for r in range(rows):
        for c in range(1, cols):
            matrix[r][c] += matrix[r][c - 1]
    ans = 0
    for c1 in range(cols):
        for c2 in range(c1, cols):
            seen = defaultdict(int)
            seen[0] = 1
            sm = 0

            for row in matrix:
                sm += row[c2] - (row[c1 - 1] if c1 else 0)
                needed = sm - target
                ans += seen[needed]
                seen[sm] += 1

    return ans