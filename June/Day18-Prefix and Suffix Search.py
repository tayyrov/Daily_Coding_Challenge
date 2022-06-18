"""
Question Source:Leetcode
Level: Hard
Topic: String
Solver: Tayyrov
Date: 18.06.2022
"""
from collections import defaultdict
from typing import List


class WordFilter:

    def __init__(self, words: List[str]):
        self.dic = defaultdict(int)
        for idx, w in enumerate(words):
            ln = min(10, len(w)) + 1

            for i in range(1, ln):
                for j in range(1, ln):
                    self.dic[(w[:i]) + "." + w[-j:]] = idx

    def f(self, prefix: str, suffix: str) -> int:
        curr_pair = prefix + "." + suffix
        if  curr_pair in self.dic:
            return self.dic[curr_pair]
        return -1

"""
Time: 100 * O(N) where N is the number of words
Space: 100 * O(N)
"""

