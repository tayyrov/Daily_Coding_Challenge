"""
Question Source:Leetcode
Level: Easy
Topic: Heap
Solver: Tayyrov
Date: 07.04.2022
"""

from heapq import heapify, heappop, heappush
from typing import List


def lastStoneWeight(stones: List[int]) -> int:
    stones = [-i for i in stones]
    heapify(stones)

    while len(stones) > 1:
        one = -heappop(stones)
        two = -heappop(stones)

        dif = one - two

        if dif:
            heappush(stones, -dif)
        print(stones)
    return -stones[0] if stones else 0

"""
Time complexity: O(NlogN)
Space complexity: O(N)
"""