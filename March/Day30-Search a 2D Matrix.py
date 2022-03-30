"""
Question Source:Leetcode
Level: Medium
Topic: Binary search
Solver: Tayyrov
Date: 30.03.2022
"""
from typing import List


def searchMatrix(matrix: List[List[int]], target: int) -> bool:
    r, c = len(matrix), len(matrix[0])

    left, right = 0, r * c - 1

    def convert(num):
        row, col = num // c, num % c
        return matrix[row][col]

    while left <= right:
        mid = (left + right) // 2
        num = convert(mid)

        if num < target:
            left = mid + 1
        elif num > target:
            right = mid - 1
        else:
            return True

    return False