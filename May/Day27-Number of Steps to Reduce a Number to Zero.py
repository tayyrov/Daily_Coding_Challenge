"""
Question Source:Leetcode
Level: Easy
Topic: Math
Solver: Tayyrov
Date: 27.05.2022
"""


def numberOfSteps(num: int) -> int:
    ans = 0

    while num > 0:
        if num % 2 == 0:
            num //= 2
        else:
            num -= 1
        ans += 1
    return ans

