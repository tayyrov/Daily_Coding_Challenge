"""
Question Source: https://leetcode.com/problems/maximum-xor-of-two-numbers-in-an-array/
Level: Medium
Topic: Bit Manipulation
Solver: Tayyrov
Date: 01.27.2022
"""
from typing import *

def findMaximumXOR(nums: List[int]) -> int:
    ans = 0
    mask = 0
    # instead of iterating 32 bit we can take the maximum number and len of its binary represenattion
    max_len = len(bin(max(nums))[2:])
    # iteration starts from the first digit in binary representation of number and go to the right
    for i in reversed(range(max_len)):
        # currently needed bit
        mask |= 1 << i
        # set of all possible starts of numbers, using num & mask: first iterations first digit, on the next one
        # first two digits etc
        sets = set([mask & num for num in nums])

        temp = ans | 1 << i
        # check if the bit can be made from the numbers in the current set
        for num in sets:
            if temp ^ num in sets:
                ans = temp
                break

    return ans

"""
Time Complexity: 0(32N) -> O(N)
Space Complexity: O(N)
"""