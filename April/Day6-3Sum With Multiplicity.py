"""
Question Source:Leetcode
Level: Medium
Topic: Hash table
Solver: Tayyrov
Date: 06.04.2022
"""

from collections import Counter
from typing import List


def threeSumMulti(arr: List[int], target: int) -> int:
    ans = 0
    count = Counter()
    MOD = 10**9 + 7
    ln = len(arr)
    for i in range(ln):
        for j in range(i + 1, ln):
            needed = target - arr[i] - arr[j]
            if needed in count:
                ans += count[needed]
        count[arr[i]] += 1
    return ans % MOD

"""
Time complexity: O(N^2)
Space complexity: O(N)
"""