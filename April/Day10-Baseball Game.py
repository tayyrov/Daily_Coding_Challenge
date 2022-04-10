"""
Question Source:Leetcode
Level: Easy
Topic: Stack
Solver: Tayyrov
Date: 10.04.2022
"""
from typing import List


def calPoints(ops: List[str]) -> int:
    stack = []

    for char in ops:
        if char == "+":
            stack.append(stack[-2] + stack[-1])
        elif char == "D":
            stack.append(stack[-1] * 2)
        elif char == "C":
            stack.pop()
        else:
            stack.append(int(char))

    return sum(stack)
"""
Time complexity: O(N)
Space complexity: O(N)
"""