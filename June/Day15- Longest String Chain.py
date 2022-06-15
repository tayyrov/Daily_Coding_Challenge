"""
Question Source:Leetcode
Level: Medium
Topic: DP
Solver: Tayyrov
Date: 15.06.2022
"""
from typing import List


def longestStrChain(words: List[str]) -> int:
    def is_match(s1, s2):
        ln1 = len(s1) - 1
        ln2 = len(s2) - 1

        if ln1 != ln2 - 1:  # one char has to be removed so this check is must
            return False

        while ln1 >= 0 and ln2 >= 0:
            if s1[ln1] == s2[ln2]:
                ln1 -= 1
                ln2 -= 1
            else:
                return s1[:ln1 + 1] == s2[:ln2]
        return True

    ln = len(words)

    dp = [1] * ln  # max chain len that ends with this particular word

    # sorting is important so that it can be ched with the smaller len words, becoz this can be only results
    words.sort(key=lambda x: len(x))
    for i in range(ln):
        best = 1
        for j in range(i):
            # best = 1
            if is_match(words[j], words[i]):
                best = max(best, dp[j] + 1)  # whcih of them has already the longest chain so take that
        dp[i] = best
    # print(words)
    # print(dp)
    return max(dp)

"""
Time: O(N^2 * M) where N is the len of words and m is the len of max word len
Space: O(N)
"""