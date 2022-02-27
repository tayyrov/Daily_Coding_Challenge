"""
Question Source:Leetcode
Level: Hard
Topic: Bitmask, DP
Solver: Tayyrov
Date: 26.02.2022
"""
from collections import deque
from typing import List


def shortestPathLength(self, graph: List[List[int]]) -> int:
    #         nodes = [n for n in range(len(graph))]
    #         q = deque([(n, {n}, 0) for n in nodes])
    #         st = set(nodes)

    #         seen = set([(n, n) for n in nodes])
    #         while q:
    #             curr, path, step = q.popleft()

    #             if path == st:
    #                 return step

    #             for nei in graph[curr]:
    #                 # tuple can be cached as it is immutable but list cant so we make tuple
    #                 x = tuple([nei] + sorted(path|{nei}))
    #                 if x not in seen:
    #                     q.append((nei, path|{nei}, step+1))
    #                     seen.add(x)

    # insted of making tuple etc, we can use mitmask as strngs are also immutable hence it can be used as a key for dics/sets

    nodes = [n for n in range(len(graph))]
    # for each node labeling that particular node as visited by doing 1 << n
    q = deque([(n, 1 << n, 0) for n in nodes])
    seen = {(n, 1 << n) for n in nodes}
    final = (1 << len(
        graph)) - 1  # means if n == 4 then 1 << 4 == 10000 and minus 1 will make this 1111 in binary hence all 4 nedes visited

    while q:
        curr, status, step = q.popleft()

        if status == final:
            return step

        for nei in graph[curr]:
            new_status = status | (1 << nei)
            if (nei, new_status) not in seen:
                q.append((nei, new_status, step + 1))
                seen.add((nei, new_status))