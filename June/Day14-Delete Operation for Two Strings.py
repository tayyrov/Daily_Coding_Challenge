"""
Question Source:Leetcode
Level: Medium
Topic: DP
Solver: Tayyrov
Date: 14.06.2022
"""


def minDistance(word1: str, word2: str) -> int:
    l = len(word1)
    w = len(word2)

    dp = [[0] * (w + 1) for _ in range(l + 1)]
    #find longest common subsequence and rest should be removed from both strings
    for i in range(1, l + 1):
        for j in range(1, w + 1):
            if word1[i - 1] == word2[j - 1]:
                dp[i][j] = 1 + dp[i - 1][j - 1]
            else:
                dp[i][j] = max(dp[i - 1][j], dp[i][j - 1])

    return l + w - 2 * dp[-1][-1]

"""
Time: O(NxM)
Space: O(NxM)
"""