"""
Question Source: https://leetcode.com/problems/best-time-to-buy-and-sell-stock/
Level: Easy
Topic: Array
Solver: Tayyrov
Date: 02.01.2022
"""
from typing import *


def maxProfit(prices: List[int]) -> int:
    mx = 0
    ans = 0
    for n in prices[::-1]:
        if n > mx:
            mx = n
        elif n < mx:
            ans = max(ans, mx - n)
    return ans


"""
Time = O(N)
Space: O(1)
"""
