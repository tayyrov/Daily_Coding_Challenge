"""
Question Source:Leetcode
Level: Hard
Topic: heap, pq
Solver: Tayyrov
Date: 23.06.2022
"""
from heapq import heappush, heappop
from typing import List


def scheduleCourse(courses: List[List[int]]) -> int:
    sor = sorted(courses, key=lambda x: x[1])

    taken = []

    curr_time = 0

    for dur, end in sor:
        heappush(taken, -dur)
        curr_time += dur
        if curr_time > end:
            largest = heappop(taken)
            curr_time += largest  # this will be substaction as largest is negative num

    return len(taken)