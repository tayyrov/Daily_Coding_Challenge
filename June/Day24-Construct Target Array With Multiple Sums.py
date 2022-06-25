"""
Question Source:Leetcode
Level: Hard
Topic: heap, pq
Solver: Tayyrov
Date: 24.06.2022
"""
from heapq import heappush, heappop, heapify
from typing import List


def isPossible(self, target: List[int]) -> bool:
    heap = [-n for n in target]
    heapify(heap)
    sm = sum(target)
    while heap[0] != -1:
        curr = -heappop(heap)
        sm -= curr
        if sm == 1:
            return True
        if sm >= curr or sm == 0 or curr % sm == 0:
            return False
        curr %= sm
        sm += curr
        heappush(heap, -curr)
    return True
