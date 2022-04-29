"""
Question Source:Leetcode
Level: Medium
Topic: BFS
Solver: Tayyrov
Date: 29.04.2022
"""
from typing import List


def isBipartite(graph: List[List[int]]) -> bool:
    seen = {}
    for node in range(len(graph)):
        if node not in seen:
            seen[node] = 0
            stack = [node]

            while stack:
                cur = stack.pop()
                for nei in graph[cur]:
                    if nei not in seen:
                        stack.append(nei)
                        seen[nei] = seen[cur] ^ 1
                    else:
                        if seen[nei] == seen[cur]:
                            return False
    return True
