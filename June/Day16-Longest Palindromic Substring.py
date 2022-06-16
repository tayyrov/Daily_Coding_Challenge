"""
Question Source:Leetcode
Level: Medium
Topic: DP
Solver: Tayyrov
Date: 15.06.2022
"""


def longestPalindrome(s: str) -> str:
    ans = ""
    best = 0
    ln = len(s)
    for i in range(ln):

        # odd len palindromes
        left = right = i
        while left >= 0 and right < ln and s[left] == s[right]:
            if right - left + 1 > best:
                best = right - left + 1
                ans = s[left:right + 1]

            left -= 1
            right += 1

        # even len palindromes
        left, right = i, i + 1
        while left >= 0 and right < ln and s[left] == s[right]:
            if right - left + 1 > best:
                best = right - left + 1
                ans = s[left:right + 1]

            left -= 1
            right += 1
    return ans

"""
Time: O(N^2) where N is the len of s
Space: O(1)
"""