"""
Question Source: https://leetcode.com/problems/can-place-flowers/
Level: Easy
Topic: Greedy
Solver: Tayyrov
Date: 01.18.2022
"""

from typing import *


def canPlaceFlowers(flowerbed: List[int], n: int) -> bool:
    flowerbed = [0] + flowerbed + [0]

    #         for num, group in groupby(flowerbed):
    #             if num == 0:
    #                 n -= (len(list(group))-1)//2
    #         return n < 1

    # solution 2 without groupby
    ln = len(flowerbed)

    for idx in range(1, ln - 1):
        if flowerbed[idx - 1] == flowerbed[idx] == flowerbed[idx + 1]:
            n -= 1
            flowerbed[idx] = 1

    return n <= 0

"""
Time complexity = O(N)
Space Complexity = O(1)
"""