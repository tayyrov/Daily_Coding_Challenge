"""
Question Source:Leetcode
Level: Medium
Topic: Greedy
Solver: Tayyrov
Date: 20.03.2022
"""
from collections import Counter
from math import inf
from typing import List


def minDominoRotations(tops: List[int], bottoms: List[int]) -> int:
    ans = inf
    top_count = Counter(tops)
    bottom_count = Counter(bottoms)
    ln = len(tops)
    for n in range(1, 7):
        valid = True
        for i, j in zip(tops, bottoms):
            if i != n and j != n:
                valid = False
                break
        if valid:
            ans = min(ans, ln - max(top_count[n], bottom_count[n]))

    return -1 if ans == inf else ans