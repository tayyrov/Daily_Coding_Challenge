"""
Question Source:Leetcode
Level: Easy
Topic: Stack
Solver: Tayyrov
Date: 01.05.2022
"""
from typing import List

def backspaceCompare(s: str, t: str) -> bool:
    def solve(s):
        stack = []

        for char in s:
            if char.isalpha():
                stack.append(char)
            else:
                if stack:
                    stack.pop()
        return stack

    return solve(s) == solve(t)