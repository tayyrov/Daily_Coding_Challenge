"""
Question Source: https://leetcode.com/problems/word-pattern/
Level: Easy
Topic: Hash Map
Solver: Tayyrov
Date: 01.17.2022
"""


def wordPattern(pattern: str, s: str) -> bool:
    s = s.split()
    if len(s) != len(pattern):
        return False

    matched_letters = {}
    matched_words = {}
    for letter, word in zip(pattern, s):
        if letter in matched_letters and matched_letters[letter] != word:
            return False
        if word in matched_words and matched_words[word] != letter:
            return False
        matched_letters[letter] = word
        matched_words[word] = letter

    return True
"""
Time complexity = O(N)
Space Complexity = O(N+M)  -> N is the length of the pattern M is length of s
"""
