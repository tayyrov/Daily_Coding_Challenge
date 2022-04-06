"""
Question Source:Leetcode
Level: Medium
Topic: Two pointer
Solver: Tayyrov
Date: 05.04.2022
"""
from typing import List


def maxArea(height: List[int]) -> int:
    left = 0
    right = len(height) - 1
    ans = 0
    while left < right:
        dis = right - left
        h = min(height[left], height[right])
        ans = max(ans, dis * h)

        if height[left] < height[right]:
            left += 1
        else:
            right -= 1

    return ans

"""
Time complexity: O(N)
Space complexity: O(1)
"""