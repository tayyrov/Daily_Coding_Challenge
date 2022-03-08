"""
Question Source:Leetcode
Level: Hard
Topic: Combinatorics
Solver: Tayyrov
Date: 06.03.2022
"""
from typing import List
from math import factorial


def countOrders(n: int) -> int:
    return (factorial(2 * n) // 2 ** n) % (10 ** 9 + 7)
