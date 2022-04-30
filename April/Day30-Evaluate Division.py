"""
Question Source:Leetcode
Level: Medium
Topic: DFS, Graph
Solver: Tayyrov
Date: 30.04.2022
"""

from collections import defaultdict
from typing import List


def calcEquation(equations: List[List[str]], values: List[float], queries: List[List[str]]) -> List[float]:
    graph = defaultdict(list)

    for idx, (a, b) in enumerate(equations):
        graph[a].append((b, values[idx]))
        graph[b].append((a, 1/ values[idx]))

    ans = []
    for start, end in queries:
        if start == end:
            if start in graph:
                ans.append(1)
            else:
                ans.append(-1)
        else:
            stack = [(start, 1)]
            find = False
            visited = {start}
            while stack:

                curr, value = stack.pop()

                if curr == end:
                    ans.append(value)
                    find = True
                else:
                    for nei, factor in graph[curr]:
                        if nei not in visited:
                            visited.add(nei)
                            stack.append((nei, value * factor))
            if not find:
                ans.append(-1)
    return ans