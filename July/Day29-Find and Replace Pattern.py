"""
Question Source:Leetcode
Level: Medium
Topic: Hash-Map
Solver: Tayyrov
Date: 29.07.2022
"""
from typing import List


def findAndReplacePattern(words: List[str], pattern: str) -> List[str]:
    def isvalid(s1, s2):
        s1_lookup = dict()
        s2_lookup = dict()

        for char1, char2 in zip(s1, s2):
            if char1 in s1_lookup:
                if char2 not in s2_lookup or s2_lookup[char2] != char1:
                    return False
            if char2 in s2_lookup:
                if char1 not in s1_lookup or s1_lookup[char1] != char2:
                    return False
            else:
                s1_lookup[char1] = char2
                s2_lookup[char2] = char1
        return True

    ans = []

    for word in words:
        if isvalid(word, pattern):
            ans.append(word)

    return ans
