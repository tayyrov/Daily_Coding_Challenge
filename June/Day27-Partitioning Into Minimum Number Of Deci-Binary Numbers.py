"""
Question Source:Leetcode
Level: Medium
Topic: Greedy
Solver: Tayyrov
Date: 27.06.2022
"""


def minPartitions(n: str) -> int:
    return int(max(n)[-1])

"""
Time: O(N) where N is the len of n
Space: O(1)
"""