"""
Question Source:Leetcode
Level: Medium
Topic: Array
Solver: Tayyrov
Date: 03.04.2022
"""
from typing import List


def nextPermutation(nums: List[int]) -> None:
    """
    Do not return anything, modify nums in-place instead.
    """

    ln = len(nums)

    for i in range(ln - 1, 0, -1):
        if nums[i - 1] < nums[i]: # 1 3 5 4 3 2 1 this find pivot index which is index of 5
            pivot = i
            break
    else: # means nums is reversely sorted so no next largest permutation, hence we return beginning (the smallest lex)
        nums.sort()
        return
    i = ln - 1 # this needs to be changed with the most right but bigger element, in works case the pivot element
    while nums[i] <= nums[pivot - 1]:
        i -= 1
    # next permutation
    nums[pivot - 1], nums[i] = nums[i], nums[pivot - 1]
    # make the rest of the elements smallest possible so, sort increasing order in place
    nums[pivot:] = sorted(nums[pivot:])

"""
Time complexity: O(N)
Space complexity: O(1)
"""