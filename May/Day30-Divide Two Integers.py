"""
Question Source:Leetcode
Level: Medium
Topic: set
Solver: Tayyrov
Date: 30.05.2022
"""


def divide(dividentt: int, divisorr: int) -> int:
    divident = abs(dividentt)
    divisor = abs(divisorr)

    ans = 0

    while divident >= divisor:
        ans += 1
        divident -= divisor
        mul = 1
        temp = divisor
        while divident >= temp:
            divident -= temp
            ans += mul
            mul += mul
            temp += temp

    if (dividentt > 0 and divisorr < 0) or (dividentt < 0 and divisorr > 0):
        ans = -ans

    return min(max(-2147483648, ans), 2147483647)