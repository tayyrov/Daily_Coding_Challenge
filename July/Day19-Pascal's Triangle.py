"""
Question Source:Leetcode
Level: Easy
Topic: Stimulation
Solver: Tayyrov
Date: 19.07.2022
"""

from typing import List


def generate(numRows: int) -> List[List[int]]:
    ans = []

    for _ in range(numRows):
        if not ans:
            ans.append([1])
        else:
            curr = ans[-1]
            ln = len(curr)
            temp = [1]

            for i in range(1, ln):
                temp.append(curr[i - 1] + curr[i])
            temp.append(1)
            ans.append(temp)

    return ans