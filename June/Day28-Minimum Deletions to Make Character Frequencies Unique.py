"""
Question Source:Leetcode
Level: Medium
Topic: Greedy
Solver: Tayyrov
Date: 25.06.2022
"""
from collections import Counter


def minDeletions(s: str) -> int:
    cnt = Counter(s)

    seen = set()

    sor = sorted(cnt.values())[::-1]

    ans = 0
    for n in sor:
        while n in seen and n != 0:
            n -= 1
            ans += 1
        seen.add(n)
    return ans