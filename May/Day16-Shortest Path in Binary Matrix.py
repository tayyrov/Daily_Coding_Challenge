"""
Question Source:Leetcode
Level: Medium
Topic: BFS
Solver: Tayyrov
Date: 16.05.2022
"""
from collections import deque
from typing import List


def shortestPathBinaryMatrix(grid: List[List[int]]) -> int:
    cols = len(grid[0])
    rows = len(grid)
    target = (rows - 1, cols - 1)

    if grid[0][0] == 1:
        return -1

    def is_valid(r, c):
        return 0 <= r < rows and 0 <= c < cols

    q = deque([(1, 0, 0)])

    directions = [(1, 1), (1, 0), (0, 1), (-1, 1), (1, -1), (0, -1), (-1, 0), (-1, -1)]
    explored = {(0, 0)}
    while q:
        ans, row, col = q.popleft()

        if (row, col) == target:
            return ans

        for dr, dc in directions:
            nr, nc = row + dr, col + dc

            if is_valid(nr, nc) and grid[nr][nc] == 0 and (nr, nc) not in explored:
                q.append((ans + 1, nr, nc))
                explored.add((nr, nc))

    return -1