"""
Question Source:Leetcode
Level: Easy
Topic: Array
Solver: Tayyrov
Date: 11.04.2022
"""
from typing import List


def shiftGrid(grid: List[List[int]], k: int) -> List[List[int]]:
    rows = len(grid)
    cols = len(grid[0])
    k %= (rows * cols)
    if not k:
        return grid
    arr = []

    for row in grid:
        arr.extend(row)

    shifted = arr[-k:] + arr[:-k]
    ans = []
    for i in range(0, len(shifted), cols):
        ans.append(shifted[i:i + cols])

    return ans