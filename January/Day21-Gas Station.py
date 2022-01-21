"""
Question Source: https://leetcode.com/problems/gas-station/
Level: Medium
Topic: Greedy
Solver: Tayyrov
Date: 01.21.2022
"""
from typing import *


def canCompleteCircuit(gas: List[int], cost: List[int]) -> int:
    # if total of gas >= cost => it is possible to make the circle otherwise not

    if sum(cost) > sum(gas):
        return -1

    start = 0
    curr_gas = 0

    for i, (g, c) in enumerate(zip(gas, cost)):

        curr_gas += (g - c)
        # when it is minus then the start position was not ideal, and current i also not good because it is what
        # brought it to negative so we start from i+1 for the time being
        if curr_gas < 0:
            curr_gas = 0
            start = i + 1
    return start


"""
Time complexity: O(N)
Space complexity: O(1)
"""
