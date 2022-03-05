"""
Question Source:Leetcode
Level: Medium
Topic: DP
Solver: Tayyrov
Date: 05.03.2022
"""
from typing import List
from collections import Counter

def deleteAndEarn(nums: List[int]) -> int:

    cnt = Counter(nums)

    sor = sorted(set(nums))

    earn1, earn2 = 0, 0

    for i in range(len(sor)):
        curr = sor[i] * cnt[sor[i]]

        temp = earn2

        if i > 0 and sor[i] == sor[i - 1] + 1:
            earn2 = max(earn2, earn1 + curr)
        else:
            earn2 += curr
        earn1 = temp

    return earn2
"""
Time: O(nlogn) where n is the number of unique elements
Space: O(1)
"""