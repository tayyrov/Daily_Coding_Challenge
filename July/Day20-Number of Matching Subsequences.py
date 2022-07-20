"""
Question Source:Leetcode
Level: Medium
Topic: binary search + hashmap
Solver: Tayyrov
Date: 20.07.2022
"""

from bisect import bisect_right
from collections import defaultdict
from typing import List


def numMatchingSubseq(s: str, words: List[str]) -> int:
    lookup = defaultdict(list)

    for idx, char in enumerate(s):
        lookup[char].append(idx)

    ans = 0
    for word in words:
        prev = -1
        for char in word:
            if char not in lookup:
                break
            curr = lookup[char]
            next_idx = bisect_right(curr, prev)
            if next_idx >= len(curr):
                break
            prev = curr[next_idx]
        else:
            ans += 1

    return ans
