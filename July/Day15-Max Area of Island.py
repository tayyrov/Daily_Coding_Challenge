"""
Question Source:Leetcode
Level: Medium
Topic: DFS
Solver: Tayyrov
Date: 15.07.2022
"""

from typing import List

def maxAreaOfIsland(grid: List[List[int]]) -> int:
    rows = len(grid)
    cols = len(grid[0])

    def is_valid(r, c):
        return 0 <= r < rows and 0 <= c < cols

    directions = [(1, 0), (0, 1), (-1, 0), (0, -1)]

    best = 0
    for row in range(rows):
        for col in range(cols):
            if grid[row][col] == 1:
                temp = 1
                grid[row][col] = 0
                stack = [(row, col)]
                while stack:
                    curr_r, curr_c = stack.pop()
                    for x, y in directions:
                        new_r, new_c = curr_r + x, curr_c + y
                        if is_valid(new_r, new_c) and grid[new_r][new_c] == 1:
                            grid[new_r][new_c] = 0
                            stack.append((new_r, new_c))
                            temp += 1
                best = max(best, temp)

    return best