"""
Question Source:Leetcode
Level: Medium
Topic: DP
Solver: Tayyrov
Date: 09.07.2022
"""
from _heapq import heappush
from heapq import heappop
from typing import List


def maxResult(nums: List[int], k: int) -> int:
    ln = len(nums)

    heap = []

    dp = [0] * ln

    for i, n in enumerate(nums):
        temp = n
        valid = i - k
        if heap:
            while True:
                if heap[0][1] >= valid:
                    temp += -heap[0][0]
                    break
                else:
                    heappop(heap)

        heappush(heap, (-temp, i))
        dp[i] = temp
    return dp[-1]
