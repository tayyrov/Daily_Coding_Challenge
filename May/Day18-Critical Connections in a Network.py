"""
Question Source:Leetcode
Level: Medium
Topic: DFS
Solver: Tayyrov
Date: 18.05.2022
"""

import collections
from typing import List


def criticalConnections(n: int, connections: List[List[int]]) -> List[List[int]]:
    def dfs(rank, curr, prev):
        low[curr] = rank
        result = []
        for neighbor in edges[curr]:
            if neighbor == prev:
                continue
            if not low[neighbor]:
                result += dfs(rank + 1, neighbor, curr)
            low[curr] = min(low[curr], low[neighbor])
            if low[neighbor] >= rank + 1:
                result.append([curr, neighbor])
        return result

    low, edges = [0] * n, collections.defaultdict(list)
    for s, e in connections:
        edges[s].append(e)
        edges[e].append(s)

    return dfs(1, 0, -1)
