"""
Question Source: https://leetcode.com/problems/permutation-in-string/
Level: Medium
Topic: Hash Map, sliding window
Solver: Tayyrov
Date: 11.02.2022
"""
from collections import Counter


def checkInclusion(self, s1: str, s2: str) -> bool:
    left = 0
    count1 = Counter(s1)
    count2 = Counter()
    for right, char in enumerate(s2):
        count2[char] += 1

        while right - left +1 > len(s1):
            count2[s2[left]] -= 1
            if count2[s2[left]] == 0:
                del count2[s2[left]]
            left += 1
        if count1 == count2:
            return True

    return False
