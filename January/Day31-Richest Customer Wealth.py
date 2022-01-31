"""
Question Source: https://leetcode.com/problems/richest-customer-wealth/
Level: Easy
Topic: Matrix
Solver: Tayyrov
Date: 01.31.2022
"""
from typing import *


def maximumWealth(accounts: List[List[int]]) -> int:
    return max(sum(row) for row in accounts)
"""
Time: O(N*M)
Space: O(N)
"""