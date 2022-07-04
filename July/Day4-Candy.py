"""
Question Source:Leetcode
Level: Hard
Topic: Greedy
Solver: Tayyrov
Date: 4.07.2022
"""

from typing import List


def candy(ratings: List[int]) -> int:
    ln = len(ratings)

    ans = [1] * ln

    for i in range(1, ln):
        if ratings[i] > ratings[i - 1]:
            ans[i] = ans[i - 1] + 1
    for i in range(ln - 1, 0, -1):
        if ratings[i - 1] > ratings[i]:
            ans[i - 1] = max(ans[i - 1], ans[i] + 1)

    return sum(ans)

"""
Time: O(N)
Space: O(N)
"""