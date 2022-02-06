"""
Question Source: https://leetcode.com/problems/remove-duplicates-from-sorted-array-ii/
Level: Medium
Topic: Two Pointers
Solver: Tayyrov
Date: 06.02.2022
"""
from typing import *

def removeDuplicates(self, nums: List[int]) -> int:
    len_of_nums = len(nums)
    if len_of_nums < 3:
        return len_of_nums

    prev_prev = 0  # number located two step upstream of the next to be checked number
    to_be_checked = 2  # we can start checking form the third number as even the first two are teh same it doesnt
    # break the rule

    for number in nums[2:]:
        if number != nums[prev_prev]:
            prev_prev += 1
            nums[to_be_checked] = number
            to_be_checked += 1

    return to_be_checked

"""
Time : O(N) where N is length of the list
Space: O(1) 
 """