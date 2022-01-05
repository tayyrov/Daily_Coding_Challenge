"""
Question Source: https://leetcode.com/problems/palindrome-partitioning/
Level: Medium
Topic: Backtracking
Solver: Tayyrov
Date: 01.05.2022
"""
from typing import *


def palindrome_partition(s: str) -> List[List[str]]:
    partitioned_result = []

    def dfs(i, partition):
        if i == len(s):  # means we reached the end of the string without failing the requirment
            partitioned_result.append(partition[:])
            return
        for j in range(i, len(s)):
            substring = s[i:j + 1]
            # if the substring is palindrome then we add it to the partition and continue recursively searching for
            # th rest of the string
            if substring == substring[::-1]:
                dfs(j + 1, partition + [substring])

    dfs(0, [])
    return partitioned_result

def check():
    assert palindrome_partition("aab") == [["a","a","b"],["aa","b"]]
    assert palindrome_partition("a") == [["a"]]
    print("All run is OK")


check()
