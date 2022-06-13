"""
Question Source:Leetcode
Level: Medium
Topic: DP
Solver: Tayyrov
Date: 13.06.2022
"""

from typing import List


def minimumTotal(triangle: List[List[int]]) -> int:
    curr_level = len(triangle) - 1
    while curr_level > 0:
        curr_level -= 1
        for i, n in enumerate(triangle[curr_level]):
            triangle[curr_level][i] += min(triangle[curr_level + 1][i], triangle[curr_level + 1][i + 1])

    return triangle[0][0]

"""
Time: O(N) N is the total number of elements in a triangle
Space: O(1) since the triangle modified in place
"""