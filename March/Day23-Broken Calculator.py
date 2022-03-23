"""
Question Source:Leetcode
Level: Medium
Topic: Greedy
Solver: Tayyrov
Date: 23.03.2022
"""


def brokenCalc(s: int, target: int) -> int:
    steps = 0
    while s != target:
        if s > target:
            steps += (s - target)
            break
        else:
            if target % 2 == 1:
                target += 1
            else:
                target //= 2

            steps += 1

    return steps
