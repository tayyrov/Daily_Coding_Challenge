"""
Question Source: https://leetcode.com/problems/k-diff-pairs-in-an-array/
Level: Medium
Topic: Hash Map
Solver: Tayyrov
Date: 09.02.2022
"""
from collections import Counter
from typing import *


def findPairs(nums: List[int], k: int) -> int:
    count = Counter(nums)
    ans = 0

    for n in count:
        needed = n + k
        if needed in count:
            if needed == n:
                if count[needed] > 1:
                    ans += 1
            else:
                ans += 1

    return ans

"""
Time: O(N) number of all element due to counting
Space: O(k) number of unique elements
"""
