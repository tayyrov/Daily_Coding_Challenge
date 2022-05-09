"""
Question Source:Leetcode
Level: Medium
Topic: Backtracking
Solver: Tayyrov
Date: 09.05.2022
"""
from typing import List


def letterCombinations(digits: str) -> List[str]:
    lets = {"2": "abc", "3": "def", "4": "ghi", "5": "jkl", "6": "mno", "7": "pqrs", "8": "tuv", "9": "wxyz"}

    if not digits:
        return []
    ans = [""]

    for num in digits:
        curr = lets[num]
        temp = []
        for s in ans:
            for let in curr:
                temp.append(s + let)

        ans = temp[::-1]

    return ans