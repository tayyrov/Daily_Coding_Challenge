"""
Question Source:Leetcode
Level: Medium
Topic: Greedy
Solver: Tayyrov
Date: 24.03.2022
"""
from typing import List


def numRescueBoats(people: List[int], limit: int) -> int:
    people.sort()
    left = 0
    right = len(people) - 1
    needed_boat = 0
    while left <= right:
        if people[left] + people[right] <= limit:
            left += 1
            right -= 1
        else:
            right -= 1

        needed_boat += 1

    return needed_boat

