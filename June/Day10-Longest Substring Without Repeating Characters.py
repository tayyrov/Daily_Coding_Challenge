"""
Question Source:Leetcode
Level: Medium
Topic: Two pointers
Solver: Tayyrov
Date: 10.06.2022
"""


def lengthOfLongestSubstring(s: str) -> int:
    left = 0
    seen = set()
    longest_substring_len = 0
    for right, char in enumerate(s):

        while char in seen:
            seen.remove(s[left])
            left += 1
        seen.add(char)
        longest_substring_len = max(longest_substring_len, right - left + 1)

    return longest_substring_len

"""
Time: O(n) where n is the len(s)
Space: O(n) where n is the len(s)
"""
