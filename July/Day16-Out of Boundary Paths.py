"""
Question Source:Leetcode
Level: Medium
Topic: DP
Solver: Tayyrov
Date: 16.07.2022
"""


def findPaths(rows: int, cols: int, maxMove: int, startRow: int, startColumn: int) -> int:
    MOD = 10 ** 9 + 7
    board = [[0] * cols for _ in range(rows)]

    board[startRow][startColumn] = 1

    total = 0

    directions = [(1, 0), (0, 1), (-1, 0), (0, -1)]
    while maxMove:
        maxMove -= 1

        next_board = [[0] * cols for _ in range(rows)]

        for r in range(rows):
            for c in range(cols):
                for dr, dc in directions:
                    nr, nc = dr + r, dc + c
                    if 0 <= nr < rows and 0 <= nc < cols:
                        next_board[nr][nc] += board[r][c]
                    else:
                        total += board[r][c]

        board = next_board

    return total % MOD
