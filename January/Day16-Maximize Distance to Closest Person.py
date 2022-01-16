"""
Question Source: https://leetcode.com/problems/maximize-distance-to-closest-person/
Level: Medium
Topic: Array
Solver: Tayyrov
Date: 01.16.2022
"""
from typing import *


def maxDistToClosest(seats: List[int]) -> int:
    # the way to deal with two sides, this will work as there is at least one 1 in the array
    answer = max(seats.index(1), seats[::-1].index(1))

    zeros = 0

    for num in seats:
        if num == 0:
            zeros += 1
        else:
            zeros = 0
        answer = max(answer, (zeros + 1) // 2)

    return answer

"""
Time complexity = O(N)  -> N is the length of the input array
Space Complexity = O(1)
"""