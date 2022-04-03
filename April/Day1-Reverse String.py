"""
Question Source:Leetcode
Level: Easy
Topic: Array
Solver: Tayyrov
Date: 01.04.2022
"""
from typing import List

def reverseString(s: List[str]) -> None:
    """
    Do not return anything, modify s in-place instead.
    """
    left = 0
    right = len(s) - 1

    while left < right:
        s[left], s[right] = s[right], s[left]
        left += 1
        right -= 1

"""
Time complexity: O(N)
Space complexity: O(1)
"""