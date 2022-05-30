"""
Question Source:Leetcode
Level: Medium
Topic: set
Solver: Tayyrov
Date: 29.05.2022
"""
from collections import defaultdict
from typing import List


def maxProduct(words: List[str]) -> int:
    cnt = defaultdict(tuple)

    for w in words:
        cnt[w] = (set(w), len(w))

    ans = 0

    for i, (key, value) in enumerate(cnt.items()):
        for j, (key2, value2) in enumerate(cnt.items()):
            if j > i:
                st1 = value[0]
                st2 = value2[0]
                if st1.intersection(st2) == set():
                    ans = max(ans, value[1] * value2[1])

    return ans
