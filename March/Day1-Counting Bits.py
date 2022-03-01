"""
Question Source:Leetcode
Level: Easy
Topic: Bit Manipulation
Solver: Tayyrov
Date: 01.03.2022
"""
from typing import List


def countBits(num: int) -> List[int]:
    ans = []
    for i in range(num + 1):
        # ans.append(bin(i).count("1"))
        ct = 0
        while i > 0:
            ct += 1
            i = i & (i - 1)
        ans.append(ct)

    return ans

"""
Time complexity is O(n log n) 
Space complexity is O(1) 
"""