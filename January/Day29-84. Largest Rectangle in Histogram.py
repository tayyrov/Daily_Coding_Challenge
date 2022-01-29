"""
Question Source: https://leetcode.com/problems/largest-rectangle-in-histogram/
Level: Hard
Topic: Stack
Solver: Tayyrov
Date: 01.29.2022
"""
from typing import *


def largestRectangleArea(self, heights: List[int]) -> int:
    heights += [
        -1]  # to ensure that the last one is the smallest hence stack is popped and area is calculated when we
    # reached the end

    max_area = 0
    # store height and index together
    stack = []
    len_of_heights = len(heights)
    for idx, h in enumerate(heights):
        start = idx
        while stack and stack[-1][0] > h:
            height, index = stack.pop()
            max_area = max(max_area, height * (idx - index))
            start = index  # since we are popping the ones with has a bigger height than the current one the starting
            # index of the current height can be extended to the point where there is at least the height of current
            # one!
        stack.append(
            (h, start))  # start is not necessarily == idx at this point it might have extended to the previous
        # points where they have at least that much height

    return max_area

"""
Time complexity: O(N)
Space complexity: O(N)
"""