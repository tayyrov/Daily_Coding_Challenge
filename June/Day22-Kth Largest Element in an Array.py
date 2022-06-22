"""
Question Source:Leetcode
Level: Medium
Topic: heap, pq
Solver: Tayyrov
Date: 22.06.2022
"""
from heapq import heapify, heappop
from typing import List


def findKthLargest(nums: List[int], k: int) -> int:
    heap = [-n for n in nums]
    heapify(heap)

    while k > 1:
        heappop(heap)
        k -= 1
    return -heappop(heap)