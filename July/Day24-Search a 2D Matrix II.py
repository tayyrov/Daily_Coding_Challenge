"""
Question Source:Leetcode
Level: Medium
Topic: Binary Search
Solver: Tayyrov
Date: 24.07.2022
"""

from bisect import bisect_left
from typing import List


def searchMatrix(matrix: List[List[int]], target: int) -> bool:
    cols = len(matrix[0])
    for row in matrix:
        if row[0] > target or row[-1] < target:
            continue
        idx = bisect_left(row, target)
        if idx < cols and row[idx] == target:
            return True

    return False