"""
Question Source:Leetcode
Level: Medium
Topic: Sorting
Solver: Tayyrov
Date: 20.06.2022
"""
from typing import List


def minimumLengthEncoding(words: List[str]) -> int:
    s = ["".join(w[::-1]) for w in words]

    s.sort()

    ans = 0

    ln = len(s)

    for i in range(ln):
        if i + 1 == ln or not s[i + 1].startswith(s[i]):
            ans += len(s[i]) + 1
    return ans