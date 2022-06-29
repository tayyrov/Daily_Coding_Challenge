"""
Question Source:Leetcode
Level: Medium
Topic: Greedy
Solver: Tayyrov
Date: 29.06.2022
"""
from typing import List


def reconstructQueue(people: List[List[int]]) -> List[List[int]]:
    people.sort(key=lambda x: (-x[0], x[1]))

    ans = []

    for height, rank in people:
        ans.insert(rank, [height, rank])
        # print(ans)

    return ans

"""
Time: nlogn + n**2
Space: O(1)
"""