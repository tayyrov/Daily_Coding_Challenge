"""
Question Source:Leetcode
Level: Easy
Topic: Stack
Solver: Tayyrov
Date: 28.02.2022
"""
from typing import List


def summaryRanges(nums: List[int]) -> List[str]:
    stack = []
    ans = []
    for n in nums:
        if stack and stack[-1] + 1 < n:
            if len(stack) == 1:
                temp = str(stack.pop())
            else:
                temp = str(stack.pop(0)) + "->" + str(stack.pop())
            ans.append(temp)
            stack.append(n)
        elif not stack:
            stack.append(n)
        elif stack[-1] + 1 == n:
            if len(stack) == 1:
                stack.append(n)
            else:
                stack[-1] = n

    if len(stack) == 1:
        temp = str(stack.pop())
        ans.append(temp)
    elif len(stack) == 2:
        temp = str(stack.pop(0)) + "->" + str(stack.pop())
        ans.append(temp)

    return ans


"""
Time complexity is O(n) where n is the len of nums array. 
Space complexity is O(1), as we store maximum 2 elements in the stack.
"""
