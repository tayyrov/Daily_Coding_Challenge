"""
Question Source: https://leetcode.com/problems/minimize-deviation-in-array/
Level: Hard
Topic: Heap, Priority Queue
Solver: Tayyrov
Date: 19.02.2022
"""


from heapq import heapify, heappop, heappush
from typing import List


def minimumDeviation(nums: List[int]) -> int:
    heap = []

    for n in nums:
        mn = mx = n

        while mn % 2 == 0:
            mn //= 2

        while mx % 2 == 1: # this will execute maximum once since odd number will get even after one step
            mx *= 2

        heap.append((mn, mx))

    heapify(heap)

    mx = max(i for i, j in heap) # maximum of all possible mins

    ans = float("inf")

    while len(heap) == len(nums):
        curr, limit = heappop(heap)

        ans = min(ans, mx -curr)

        if curr * 2 <= limit:
            heappush(heap, (curr *2, limit))
            # check if the newly added number will change the minimum
            mx = max(mx, 2* curr)
    return ans
"""
Time: O(NLogN)
Space: O(N)
"""