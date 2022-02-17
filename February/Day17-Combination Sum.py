"""
Question Source: https://leetcode.com/problems/combination-sum/
Level: Medium
Topic: Backtracking
Solver: Tayyrov
Date: 17.02.2022
"""

from typing import List


def combinationSum(candidates: List[int], target: int) -> List[List[int]]:
    # iterative solution : a bit messy
    #         stack =[([num], num) for num in candidates]

    #         ans = set()

    #         while stack:

    #             path, total = stack.pop()

    #             if total == target:
    #                 temp = tuple(sorted(path))
    #                 ans.add(temp)
    #                 continue
    #             if total > target:
    #                 continue

    #             for n in candidates:
    #                 if total + n <= target:
    #                     stack.append((path+[n], total + n))

    #         return [list(t) for t in ans]

    # 2.recursive solution:

    ans = []

    def dfs(total, path, idx):

        if total == target:
            ans.append(path[::])
            return
        if total > target:
            return

        for i in range(idx, len(candidates)):
            dfs(total + candidates[i], path + [candidates[i]], i)

    dfs(0, [], 0)

    return ans
