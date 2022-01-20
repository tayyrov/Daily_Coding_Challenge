"""
Question Source: https://leetcode.com/problems/koko-eating-bananas/
Level: Medium
Topic: Binary Search
Solver: Tayyrov
Date: 01.20.2022
"""

from typing import *


def minEatingSpeed(piles: List[int], h: int) -> int:
    def solve(k):
        ans = 0
        for n in piles:
            ans += (n + k - 1) // k
        return ans

    left = 1
    right = max(piles)
    result = right

    while left <= right:

        k = left + (right - left) // 2
        hours = solve(k)
        if hours <= h:  # if this is true the ans is valid, but we check if the smaller ones can be valid too
            result = k
            right = k - 1
        else:
            left = k + 1

    return result


"""
Time complexity = O(log(max(piles)*N))
Space Complexity = O(1)
"""
