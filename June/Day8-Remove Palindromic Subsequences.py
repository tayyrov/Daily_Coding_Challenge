"""
Question Source:Leetcode
Level: Easy
Topic: Arrays
Solver: Tayyrov
Date: 08.06.2022
"""

def removePalindromeSub(s: str) -> int:
    if not s:
        return 0
    if s == s[::-1]:
        return 1
    return 2
