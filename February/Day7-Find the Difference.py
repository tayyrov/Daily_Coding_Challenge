"""
Question Source: https://leetcode.com/problems/find-the-difference/
Level: Easy
Topic: Hash Table
Solver: Tayyrov
Date: 07.02.2022
"""
from collections import Counter


def findTheDifference(self, s: str, t: str) -> str:
    return list((Counter(t) - Counter(s)).keys())[0]

