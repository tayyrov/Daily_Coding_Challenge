"""
Question Source:Leetcode
Level: Medium
Topic: Backtracking
Solver: Tayyrov
Date: 11.05.2022
"""


def countVowelStrings(n: int) -> int:
    ans = list("abcde")
    n -= 1
    for _ in range(n):
        temp = []
        for word in ans:
            for char in "abcde":
                if word[-1] <= char:
                    temp.append(word + char)
        ans = temp[:]

    return len(ans)
