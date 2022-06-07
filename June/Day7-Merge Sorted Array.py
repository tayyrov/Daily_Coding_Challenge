"""
Question Source:Leetcode
Level: Easy
Topic: Arrays
Solver: Tayyrov
Date: 07.06.2022
"""
from typing import List


def merge(nums1: List[int], m: int, nums2: List[int], n: int) -> None:
    """
    Do not return anything, modify nums1 in-place instead.
    """
    # starting from the end of nums 1 place the biggest and stepstep by step forward
    # at the end if n is still not used comteletely put it infront
    start = n + m - 1
    n -= 1
    m -= 1

    while n >= 0 and m >= 0:
        if nums1[m] >= nums2[n]:
            nums1[start] = nums1[m]
            m -= 1
        else:
            nums1[start] = nums2[n]
            n -= 1
        start -= 1
    # print(nums1)
    while n >= 0:
        nums1[start] = nums2[n]
        n -= 1
        start -= 1