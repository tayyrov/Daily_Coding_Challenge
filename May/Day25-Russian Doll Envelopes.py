"""
Question Source:Leetcode
Level: Hard
Topic: Binary search
Solver: Tayyrov
Date: 25.05.2022
"""
from bisect import bisect_left
from cmath import inf
from typing import List


def maxEnvelopes(self, envelopes: List[List[int]]) -> int:
    sor = sorted(envelopes, key=lambda x: (x[0], -x[-1]))

    ans = [-inf]

    for _, h in sor:
        idx = bisect_left(ans, h)
        print(idx)
        if idx == len(ans):
            ans.append(h)
        else:
            ans[idx] = h
        print(ans)
    return len(ans) - 1