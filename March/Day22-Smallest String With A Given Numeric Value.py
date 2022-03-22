"""
Question Source:Leetcode
Level: Medium
Topic: Greedy
Solver: Tayyrov
Date: 22.03.2022
"""


def getSmallestString(n: int, k: int) -> str:
    ans = ["a"] * n

    k -= n
    i = 0
    while k:
        if k >= 25:
            ans[i] = "z"
            k -= 25
        else:
            ans[i] = chr(97 + k)
            break
        i += 1

    return "".join(ans[::-1])