"""
Question Source: https://leetcode.com/problems/jump-game-iv/
Level: Medium
Topic: BFS
Solver: Tayyrov
Date: 01.15.2022
"""
from typing import *
from collections import defaultdict, deque


def minJumps(arr: List[int]) -> int:
    target_index = len(arr) - 1

    visited_indices = set()
    visited_values = set()

    steps = 0
    index = 0

    indices = defaultdict(list)
    for i, n in enumerate(arr):
        indices[n].append(i)

    queue = deque([(index, steps)])

    while queue:
        idx, steps = queue.popleft()
        num = arr[idx]

        if idx == target_index:
            return steps

        for next_step in [idx - 1, idx + 1]:
            if next_step not in visited_indices and 0 <= next_step < len(arr):
                queue.append((next_step, steps + 1))
                visited_indices.add(next_step)

        if num in visited_values:
            continue
        visited_values.add(num)
        lst = indices[num]

        for idx in lst:
            queue.append((idx, steps + 1))
            visited_indices.add(idx)


""""
Time complexity: O(N) - every node (index) visited once
Space complexity: O(N)

"""
