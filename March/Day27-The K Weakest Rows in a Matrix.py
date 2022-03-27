"""
Question Source:Leetcode
Level: Easy
Topic: Sorting
Solver: Tayyrov
Date: 27.03.2022
"""
from typing import List


def kWeakestRows(mat: List[List[int]], k: int) -> List[int]:
    arr = [[i, sum(j)] for i, j in enumerate(mat)]

    arr.sort(key=lambda x: x[1])

    ans = [i for i, j in arr][:k]

    return ans