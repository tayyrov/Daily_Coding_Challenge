"""
Question Source:Leetcode
Level: Medium
Topic: Stack
Solver: Tayyrov
Date: 15.03.2022
"""
def minRemoveToMakeValid(s: str) -> str:
    s = list(s)
    stack = []

    for ind, char in enumerate(s):
        if char == ")":
            if stack:
                stack.pop()
            else:
                s[ind] = ""
        elif char == "(":
            stack.append(ind)
    while stack:
        s[stack.pop()] = ""

    return "".join(s)