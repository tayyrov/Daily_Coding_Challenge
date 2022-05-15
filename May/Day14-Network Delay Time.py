"""
Question Source:Leetcode
Level: Medium
Topic: Dijkstra
Solver: Tayyrov
Date: 14.05.2022
"""
import heapq
from math import inf
from collections import defaultdict
from typing import List


def networkDelayTime(times: List[List[int]], n: int, k: int) -> int:
    graph = defaultdict(list)

    for fromm, to, time in times:
        graph[fromm].append((to, time))
    visited = set()

    nodeCosts = {vertex: float(inf) for vertex in range(1, n + 1)}
    nodeCosts[k] = 0
    pq = []
    heapq.heappush(pq, (0, k))

    while pq:
        so_far_cost, node = heapq.heappop(pq)
        visited.add(node)
        for nei, next_cost in graph[node]:
            if nei in visited:
                continue
            newCost = so_far_cost + next_cost

            if nodeCosts[nei] > newCost:
                nodeCosts[nei] = newCost

                heapq.heappush(pq, (newCost, nei))
    mx = max(nodeCosts.values())
    return -1 if mx == inf else mx
