"""
Question Source:Leetcode
Level: Easy
Topic: Matrix
Solver: Tayyrov
Date: 02.06.2022
"""
from typing import List

def transpose(matrix: List[List[int]]) -> List[List[int]]:
    return [list(x) for x in zip(*matrix)]