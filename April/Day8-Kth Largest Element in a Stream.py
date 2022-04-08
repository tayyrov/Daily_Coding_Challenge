"""
Question Source:Leetcode
Level: Easy
Topic: Heap
Solver: Tayyrov
Date: 08.04.2022
"""
from heapq import heapify, heappop, heappush, heapreplace
from typing import List


class KthLargest:

    def __init__(self, k: int, nums: List[int]):
        self.nums = nums
        self.k = k
        heapify(self.nums)
        while len(self.nums) > k:
            heappop(self.nums)

    def add(self, val: int) -> int:
        if len(self.nums) < self.k:
            heappush(self.nums, val)
        elif val > self.nums[0]:  # heap[0] is index of the smallest element
            heapreplace(self.nums, val)

        return self.nums[0]

"""
Time complexity: O(N^2)
Space complexity: O(N)
"""