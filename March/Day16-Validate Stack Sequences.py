"""
Question Source:Leetcode
Level: Medium
Topic: Stack
Solver: Tayyrov
Date: 16.03.2022
"""
from typing import List


def validateStackSequences(pushed: List[int], popped: List[int]) -> bool:
    idx = 0

    stack = []

    for n in pushed:
        stack.append(n)
        needed = popped[idx]
        while idx < len(popped) and stack and needed == stack[-1]:
            stack.pop()
            idx += 1
            if idx < len(popped):
                needed = popped[idx]
        # print(stack)
    return idx == len(popped)
