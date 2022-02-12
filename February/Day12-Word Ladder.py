"""
Question Source: https://leetcode.com/problems/word-ladder/
Level: Hard
Topic: Hash Map, BFS
Solver: Tayyrov
Date: 12.02.2022
"""

from collections import defaultdict, deque
from typing import *


def ladderLength(beginWord: str, endWord: str, wordList: List[str]) -> int:
    if endWord not in wordList:
        return 0
    lookup = defaultdict(list)
    for word in wordList:
        for j in range(len(word)):
            pattern = word[:j] + "*" + word[j + 1:]
            lookup[pattern].append(word)

    q = deque([(beginWord, 1)])
    seen = {beginWord}
    while q:
        curr, step = q.popleft()
        if curr == endWord:
            return step
        for i in range(len(curr)):
            key = curr[:i] + "*" + curr[i + 1:]

            for child in lookup[key]:
                if child not in seen:
                    seen.add(child)
                    q.append((child, step + 1))

    return 0
