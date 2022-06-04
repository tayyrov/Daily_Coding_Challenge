from typing import List

"""
Question Source:Leetcode
Level: Hard
Topic: Backtracking
Solver: Tayyrov
Date: 04.06.2022
"""

def solveNQueens(n: int) -> List[List[str]]:
    used_cols = set()
    pos_diag = set()
    neg_diag = set()

    ans = []
    board = [["."] * n for _ in range(n)]

    def backtrack(r):
        if r == n:
            curr = ["".join(row) for row in board]
            ans.append(curr)
            return

        for c in range(n):
            if c not in used_cols and (r + c) not in pos_diag and (r - c) not in neg_diag:
                used_cols.add(c)
                neg_diag.add(r - c)
                pos_diag.add(r + c)
                board[r][c] = "Q"
                backtrack(r + 1)

                used_cols.remove(c)
                neg_diag.remove(r - c)
                pos_diag.remove(r + c)
                board[r][c] = "."

    backtrack(0)
    return ans