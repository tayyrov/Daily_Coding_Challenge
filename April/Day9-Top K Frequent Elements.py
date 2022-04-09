"""
Question Source:Leetcode
Level: Medium
Topic: Heap, Hash map
Solver: Tayyrov
Date: 09.04.2022
"""
from collections import Counter
from typing import List


def topKFrequent(self, nums: List[int], k: int) -> List[int]:
    cnt = Counter(nums)
    arr = cnt.most_common(k)
    return list(i for i, j in arr)