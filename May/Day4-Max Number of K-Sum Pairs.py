"""
Question Source:Leetcode
Level: Medium
Topic: Stack
Solver: Tayyrov
Date: 03.05.2022
"""
from typing import List
from collections import Counter

def maxOperations(nums: List[int], k: int) -> int:

    cnt = Counter(nums)
    ans = 0
    for n in nums:
        if cnt[n] > 0:
            needed = k - n
            if needed == n and cnt[n] == 1:
                continue
            if cnt[needed] > 0:
                ans += 1
                cnt[needed] -= 1
                cnt[n] -= 1

    return ans