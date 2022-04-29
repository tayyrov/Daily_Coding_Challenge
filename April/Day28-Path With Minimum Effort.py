"""
Question Source:Leetcode
Level: Medium
Topic: Heap
Solver: Tayyrov
Date: 28.04.2022
"""
from heapq import heapify, heappop, heappush
from typing import List


def minimumEffortPath(heights: List[List[int]]) -> int:
    rows = len(heights)
    cols = len(heights[0])
    hp = [(0, 0, 0)]
    heapify(hp)
    directions = [(1, 0), (0, 1), (-1, 0), (0, -1)]
    visited = set()
    ans = 0
    while hp:
        k, x, y = heappop(hp)
        visited.add((x, y))
        ans = max(ans, k)
        if (rows - 1, cols - 1) in visited:
            return ans
        for a, b in directions:
            nx, ny = x + a, y + b
            if 0 <= nx < rows and 0 <= ny < cols and (nx, ny) not in visited:
                new_k = abs(heights[x][y] - heights[nx][ny])
                heappush(hp, (new_k, nx, ny))