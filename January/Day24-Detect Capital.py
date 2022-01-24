"""
Question Source: https://leetcode.com/problems/detect-capital/
Level: Easy
Topic: string
Solver: Tayyrov
Date: 01.24.2022
"""


def detectCapitalUse(word: str) -> bool:
    return word == word.lower() or word == word.upper() or word == word.title()

# notes: The title() method returns a string where the first character in EVERY word is upper case
# The capitalize() method returns a string where the only first character of whole string is upper case
