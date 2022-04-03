"""
Question Source:Leetcode
Level: Easy
Topic: Array
Solver: Tayyrov
Date: 02.04.2022
"""

def validPalindrome(s: str) -> bool:

    def ispalindrome(s):
        return s == s[::-1]

    left = 0
    right = len(s) - 1

    while left < right:
        if s[left] != s[right]: # skip either left char or right char and check if it becomes palindrome
            if ispalindrome(s[:left] + s[left + 1:]) or ispalindrome(s[:right] + s[right + 1:]):
                return True
            return False
        left += 1
        right -= 1
    return True

"""
Time complexity: O(N)
Space complexity: O(1)
"""