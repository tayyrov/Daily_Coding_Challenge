"""
Question Source: https://leetcode.com/problems/find-all-anagrams-in-a-string/
Level: Easy
Topic: Sliding Window
Solver: Tayyrov
Date: 02.02.2022
"""
from typing import *
from collections import Counter


def findAnagrams(s: str, p: str) -> List[int]:
    if len(s) < len(p):
        return []
    ans = []
    left = 0
    pCount = Counter(p)
    sCount = Counter()
    for right, char in enumerate(s):
        sCount[char] += 1

        if right - left + 1 > len(p):
            sCount[s[left]] -= 1
            if sCount[s[left]] == 0:
                del sCount[s[left]]

            left += 1

        if right - left + 1 == len(p):
            if pCount == sCount:  # Since there are 26 letters this is O(1)
                ans.append(left)
    return ans


"""
Time = O(N)
Space: O(1) maximum 26 characters
"""
