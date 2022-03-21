"""
Question Source:Leetcode
Level: Medium
Topic: Hash Table
Solver: Tayyrov
Date: 21.03.2022
"""
from typing import List


def partitionLabels(s: str) -> List[int]:
    ans = []
    last_indices = {char: i for i, char in enumerate(s, start=1)}
    seen = set()
    completed = set()
    prev = 0
    for i, char in enumerate(s, start=1):
        seen.add(char)
        if last_indices[char] == i:
            completed.add(char)

        if seen == completed:
            ans.append(i - prev)
            prev = i
    return ans