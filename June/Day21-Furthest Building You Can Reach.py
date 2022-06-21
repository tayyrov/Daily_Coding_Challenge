"""
Question Source:Leetcode
Level: Medium
Topic: heap, pq
Solver: Tayyrov
Date: 21.06.2022
"""
from heapq import heappush, heappop
from typing import List


def furthestBuilding(heights: List[int], bricks: int, ladders: int) -> int:
    hp = []
    ln = len(heights)
    for i in range(ln - 1):
        step = heights[i + 1] - heights[i]
        if step > 0:
            if len(hp) >= ladders:  # means all ladders are used up, add current step and choose the smalles one and
                # try to replace it with bricks, so that the ladder can be used for a bigger step
                heappush(hp, step)
                mn = heappop(hp)
                if mn <= bricks:
                    bricks -= mn
                else:
                    return i
            else:
                heappush(hp, step)
    return ln - 1 # for index

