"""
Question Source:Leetcode
Level: Easy
Topic: Hash Map
Solver: Tayyrov
Date: 28.07.2022
"""

from collections import Counter


def isAnagram(s: str, t: str) -> bool:
    return Counter(s) == Counter(t)
