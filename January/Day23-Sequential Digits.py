"""
Question Source: https://leetcode.com/problems/sequential-digits/
Level: Medium
Topic: BFS
Solver: Tayyrov
Date: 01.23.2022
"""
from collections import deque
from typing import *


def sequentialDigits(low: int, high: int) -> List[int]:
    output = []

    q = deque(range(1, 10))

    while q:
        current_elem = q.popleft()

        if low <= current_elem <= high:
            output.append(current_elem)

        last_digit = current_elem % 10
        if last_digit < 9:
            new_elem = current_elem * 10 + last_digit + 1
            if new_elem <= high:
                q.append(new_elem)

    return output

"""There will be 9+8+...+ 1 numbers,
each requires max 1 check:
Thus, time complexity: O(45) = O(1) 
Space complexity is also O(45) = O(1). 
"""
