"""
Question Source:https://leetcode.com/problems/excel-sheet-column-number/
Level: Easy
Topic: Math
Solver: Tayyrov
Date: 22.02.2022
"""


def titleToNumber(c: str) -> int:
    exponent = 1
    ans = 0
    offset = ord("A") - 1

    for char in c[::-1]:
        ans += (ord(char) - offset) * exponent
        exponent *= 26

    return ans

"""
Time: O(N)
Space: O(1)
"""