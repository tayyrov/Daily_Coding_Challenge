"""
Question Source:Leetcode
Level: Medium
Topic: MST - Minimum Spanning Tree
Solver: Tayyrov
Date: 26.04.2022
"""
from heapq import heapify, heappop, heappush
from typing import List


def minCostConnectPoints(points: List[List[int]]) -> int:
    ln = len(points)
    arr = {i: [] for i in range(ln)}

    for i in range(ln):
        x1, y1 = points[i]

        for j in range(i + 1, ln):
            x2, y2 = points[j]

            distance = abs(x1 - x2) + abs(y1 - y2)

            arr[i].append((distance, j))
            arr[j].append((distance, i))

    ans = 0

    hp = [(0, 0)]
    heapify(hp)
    visited = set()
    while len(visited) < ln:

        cost, curr = heappop(hp)

        if curr in visited:
            continue
        visited.add(curr)
        ans += cost

        for nei_cost, nei in arr[curr]:
            if nei not in visited:
                heappush(hp, (nei_cost, nei))
    return ans
