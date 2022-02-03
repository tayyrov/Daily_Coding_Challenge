"""
Question Source: https://leetcode.com/problems/4sum-ii/
Level: Medium
Topic: Hash Table
Solver: Tayyrov
Date: 03.02.2022
"""
from typing import *
from collections import Counter


def fourSumCount(nums1: List[int], nums2: List[int], nums3: List[int], nums4: List[int]) -> int:
    #         lookup = Counter()
    #         for n1 in nums1:
    #             for n2 in nums2:
    #                 lookup[n1+n2] += 1
    #         ans = 0
    #         for n1 in nums3:
    #             for n2 in nums4:
    #                 ans += lookup[-(n1+n2)]

    #         return ans

    # solution 2

    count = Counter(n1 + n2 for n1 in nums1 for n2 in nums2)
    ans = sum(count[-n3 - n4] for n3 in nums3 for n4 in nums4)
    return ans


"""
Time: O(N^2)
Space: O(N^2)
"""
