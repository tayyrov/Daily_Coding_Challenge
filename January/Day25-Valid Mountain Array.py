"""
Question Source: https://leetcode.com/problems/valid-mountain-array/
Level: Easy
Topic: Arrays
Solver: Tayyrov
Date: 01.25.2022
"""
from typing import *


def validMountainArray(arr: List[int]) -> bool:
    ln = len(arr)
    if ln < 3:
        return False

    mx = max(arr)
    ind = arr.index(mx)

    left = ind - 1
    right = ind + 1
    if left < 0 or right > ln - 1:
        return False

    while left > -1 or right < ln:
        if left > -1:
            if arr[left + 1] <= arr[left]:
                return False
            left -= 1
        if right < ln:
            if arr[right - 1] <= arr[right]:
                return False
            right += 1

    return True
"""
Time Complexity: O(N))
Space Complexity: O(1)

"""