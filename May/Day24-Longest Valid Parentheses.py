"""
Question Source:Leetcode
Level: Hard
Topic: Stack
Solver: Tayyrov
Date: 24.05.2022
"""


def longestValidParentheses(s: str) -> int:
    stack = []

    valid_indices = []

    for index, par in enumerate(s):
        if par == ")":
            if stack and stack[-1][-1] == "(":
                valid_indices.append(stack[-1][0])
                valid_indices.append(index)
                stack.pop()
            else:
                stack.append((index, par))
        else:
            stack.append((index, par))
    st = set(valid_indices)
    ans = 0
    temp = 0

    for i in range(len(s)):
        if i in st:
            temp += 1
        else:
            temp = 0

        ans = max(ans, temp)

    return ans