"""
Question Source:Leetcode
Level: Medium
Topic: two pointer
Solver: Tayyrov
Date: 25.06.2022
"""

from math import inf
from typing import List
def maxScore(cardPoints: List[int], k: int) -> int:
    left = 0
    best = inf
    curr_sum = 0
    k = len(cardPoints) - k
    for right, number in enumerate(cardPoints):
        curr_sum += number
        if right - left + 1 > k:
            curr_sum -= cardPoints[left]
            left += 1
        if right - left + 1 == k:
            best = min(best, curr_sum)

    return sum(cardPoints) - best
