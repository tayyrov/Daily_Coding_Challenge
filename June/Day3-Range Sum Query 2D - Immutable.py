"""
Question Source:Leetcode
Level: Medium
Topic: Prefix sum
Solver: Tayyrov
Date: 03.06.2022
"""
from typing import List


class NumMatrix:

    def __init__(self, matrix: List[List[int]]):
        self.r = len(matrix)
        self.c = len(matrix[0])

        self.presum = [[0] * (self.c + 1) for _ in range(self.r + 1)]

        for r in range(1, self.r + 1):
            for c in range(1, self.c + 1):
                rr, cc = r - 1, c - 1
                self.presum[r][c] = matrix[rr][cc] + self.presum[r - 1][c] + self.presum[r][c - 1] - self.presum[r - 1][
                    c - 1]

    def sumRegion(self, row1: int, col1: int, row2: int, col2: int) -> int:

        return self.presum[row2 + 1][col2 + 1] - self.presum[row1][col2 + 1] - self.presum[row2 + 1][col1] + \
               self.presum[row1][col1]