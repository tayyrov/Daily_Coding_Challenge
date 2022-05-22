"""
Question Source:Leetcode
Level: Medium
Topic: DP
Solver: Tayyrov
Date: 22.05.2022
"""

def countSubstrings( s: str) -> int:
    def ispal(sub):
        return sub == sub[::-1]

    ans = 0
    ln = len(s)
    for i in range(ln):
        for j in range(i + 1, ln + 1):
            if ispal(s[i:j]):
                ans += 1
    return ans