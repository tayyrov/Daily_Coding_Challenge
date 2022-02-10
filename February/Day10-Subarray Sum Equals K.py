"""
Question Source: https://leetcode.com/problems/subarray-sum-equals-k/
Level: Medium
Topic: Hash Map
Solver: Tayyrov
Date: 10.02.2022
"""

from typing import *


def subarraySum(nums: List[int], k: int) -> int:
    seen = {0: 1}

    presum = 0

    ans = 0

    for n in nums:
        presum += n

        needed = presum - k

        if needed in seen:
            ans += seen[needed]
        if presum in seen:
            seen[presum] += 1
        else:
            seen[presum] = 1
    return ans

"""
Time: O(N) number of all element due to counting
Space: O(N)
"""
