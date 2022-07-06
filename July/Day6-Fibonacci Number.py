"""
Question Source:Leetcode
Level: Easy
Topic: DP
Solver: Tayyrov
Date: 6.07.2022
"""


def fib(n: int) -> int:
    seen = dict()

    def solve(n):
        if n < 2:
            return n
        if n in seen:
            return seen[n]
        curr = solve(n - 1) + solve(n - 2)
        seen[n] = curr
        return seen[n]

    return solve(n)