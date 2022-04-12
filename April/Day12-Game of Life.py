"""
Question Source:Leetcode
Level: Easy
Topic: Stimulation
Solver: Tayyrov
Date: 12.04.2022
"""
from typing import List


def gameOfLife(board: List[List[int]]) -> None:
    """
    Do not return anything, modify board in-place instead.
    """
    directions = [(1, 1), (1, 0), (0, 1), (1, -1), (-1, 1), (-1, -1), (0, -1), (-1, 0)]

    def should_die(nei):
        return nei != 2 and nei != 3

    def should_live(nei):
        return nei == 3

    def isvalid(r, c):
        return 0 <= r < rows and 0 <= c < cols

    def nei_num(r, c):
        nei = 0
        for dr, dc in directions:
            nr, nc = dr + r, dc + c
            if isvalid(nr, nc) and board[nr][nc] == 1:
                nei += 1
        return nei

    rows = len(board)
    cols = len(board[0])

    change = set()

    for r in range(rows):
        for c in range(cols):
            if board[r][c] == 0:
                nei = nei_num(r, c)
                if should_live(nei):
                    change.add((r, c))
            else:
                nei = nei_num(r, c)

                if should_die(nei):
                    change.add((r, c))

    for r in range(rows):
        for c in range(cols):
            if (r, c) in change:
                board[r][c] ^= 1

"""
Time complexity: O(N*M)
Space complexity: O(N*M)
"""