"""
Question Source:Leetcode
Level: Easy
Topic: Stack
Solver: Tayyrov
Date: 13.03.2022
"""


def isValid(s: str) -> bool:
    tokens = {("(", ")"), ("{", "}"), ("[", "]")}
    openn = {"(", "[", "{"}
    stack = []

    for char in s:
        if char in openn:
            stack.append(char)
        else:
            if not stack:
                return False
            else:
                close = stack.pop()
                if (close, char) not in tokens:
                    return False
    if stack:
        return False
    return True
