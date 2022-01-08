"""
Question Source: https://leetcode.com/problems/cherry-pickup-ii/
Level: Hard
Topic: Dynamic programming
Solver: Tayyrov
Date: 01.08.2022
"""
from typing import *


def cherryPickup(grid: List[List[int]]) -> int:
    rows = len(grid)
    cols = len(grid[0])
    calculated = {}

    def max_cherry(current_row, robot1_col,
                   robot2_col):  # The robots moving down together, hence we can us ethe same row for both
        if current_row == rows:  # means we hit the bottom of the grid
            return 0

        if (current_row, robot1_col, robot2_col) in calculated:
            return calculated[(current_row, robot1_col, robot2_col)]
        best = 0

        # if both robost are at the same cell just one of them should pick up, otherwise both pick
        if robot1_col == robot2_col:
            cherry = grid[current_row][robot1_col]
        else:
            cherry = grid[current_row][robot1_col] + grid[current_row][robot2_col]

        for dx in (-1, 0, 1):
            for dy in (-1, 0, 1):
                new_robot1_pos = robot1_col + dx
                new_robot2_pos = robot2_col + dy
                if 0 <= new_robot1_pos < cols and 0 <= new_robot2_pos < cols:  # if valid then the priveous rows cherries is added and we move the next row
                    best = max(best, max_cherry(current_row + 1, new_robot1_pos, new_robot2_pos) + cherry)

        calculated[(current_row, robot1_col, robot2_col)] = best
        return best

    return max_cherry(0, 0, cols - 1)

def check():
    assert cherryPickup([[3,1,1],[2,5,1],[1,5,5],[2,1,1]]) == 24
    assert cherryPickup([[1,0,0,0,0,0,1],[2,0,0,0,0,3,0],[2,0,9,0,0,0,0],[0,3,0,5,4,0,0],[1,0,2,3,0,0,6]]) == 28

    print("All runs are OK")
check()