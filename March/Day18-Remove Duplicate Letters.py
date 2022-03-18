"""
Question Source:Leetcode
Level: Medium
Topic: Stack
Solver: Tayyrov
Date: 18.03.2022
"""


def removeDuplicateLetters(s: str) -> str:
    last_indices = {char: idx for idx, char in enumerate(s)}

    stack = []
    added = set()
    for idx, char in enumerate(s):
        while stack and stack[-1] > char and last_indices[stack[-1]] > idx and char not in added:
            added.remove(stack.pop())

        if char not in added:
            stack.append(char)
            added.add(char)
    return "".join(stack)