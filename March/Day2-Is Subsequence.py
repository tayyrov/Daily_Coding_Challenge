"""
Question Source:Leetcode
Level: Easy
Topic: Two Pointer
Solver: Tayyrov
Date: 02.03.2022
"""


def isSubsequence(s: str, t: str) -> bool:
    current = 0
    len_s = len(s)
    if len_s == 0:
        return True

    for char in t:
        if char == s[current]:
            current += 1
            if current == len_s:
                return True

    return False

"""
Time complexity is O(n) where n is the len of s. 
Space complexity is O(1) 
"""
