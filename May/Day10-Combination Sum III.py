"""
Question Source:Leetcode
Level: Medium
Topic: Backtracking
Solver: Tayyrov
Date: 10.05.2022
"""
from typing import List


def combinationSum3(k: int, n: int) -> List[List[int]]:
    ans = []

    def dfs(start, remain, k, combo):
        if remain == 0:
            if len(combo) == k:
                ans.append(combo[:])
        if remain < 0 or len(combo) > k:
            return

        for idx in range(start, 10):
            combo.append(idx)
            # print(combo, "before")
            dfs(start + 1, remain - idx, k, combo)
            combo.pop()
            start += 1
            # print(combo, "after")

    dfs(1, n, k, [])

    return ans
