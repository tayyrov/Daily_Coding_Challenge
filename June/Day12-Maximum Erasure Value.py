"""
Question Source:Leetcode
Level: Medium
Topic: Two pointers
Solver: Tayyrov
Date: 12.06.2022
"""


from collections import Counter
from typing import List


def maximumUniqueSubarray(nums: List[int]) -> int:
    left = 0

    freq = Counter()

    curr_sum = 0
    best_sum = 0
    for right, number in enumerate(nums):

        curr_sum += number

        freq[number] += 1

        while freq[number] > 1:
            curr_sum -= nums[left]
            freq[nums[left]] -= 1
            left += 1

        best_sum = max(best_sum, curr_sum)

    return best_sum
"""
Time: O(N)
Space: O(N)
"""