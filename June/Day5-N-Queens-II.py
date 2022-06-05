"""
Question Source:Leetcode
Level: Hard
Topic: Backtracking
Solver: Tayyrov
Date: 05.06.2022
"""


def totalNQueens( n: int) -> int:
    used_cols = set()
    pos_diag = set()
    neg_diag = set()

    ans = 0

    def backtrack(r):
        if r == n:
            nonlocal ans
            ans += 1
            return

        for c in range(n):
            if c not in used_cols and (r + c) not in pos_diag and (r - c) not in neg_diag:
                used_cols.add(c)
                neg_diag.add(r - c)
                pos_diag.add(r + c)

                backtrack(r + 1)

                used_cols.remove(c)
                neg_diag.remove(r - c)
                pos_diag.remove(r + c)

    backtrack(0)
    return ans