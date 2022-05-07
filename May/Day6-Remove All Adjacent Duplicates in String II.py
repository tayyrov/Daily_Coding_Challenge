"""
Question Source:Leetcode
Level: Medium
Topic: Stack
Solver: Tayyrov
Date: 06.05.2022
"""


def removeDuplicates(s: str, k: int) -> str:
    stack = []

    for char in s:
        if not stack or stack[-1][0] != char:
            stack.append((char, 1))
        else:
            last = stack.pop()
            stack.append((last[0], last[-1] + 1))

            if stack[-1][-1] == k:
                stack.pop()

    return "".join([x * y for x, y in stack])
