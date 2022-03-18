"""
Question Source:Leetcode
Level: Medium
Topic: Stack
Solver: Tayyrov
Date: 17.03.2022
"""


def scoreOfParentheses(s: str) -> int:
    stack = [0]

    for p in s:
        if p == "(":
            stack.append(0)
        else:
            last = stack.pop()
            stack[-1] += max(1, 2 * last)
        print(stack)
    return stack[-1]
