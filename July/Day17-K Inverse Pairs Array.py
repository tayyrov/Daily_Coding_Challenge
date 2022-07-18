"""
Question Source:Leetcode
Level: Hard
Topic: DP
Solver: Tayyrov
Date: 17.07.2022
"""


def kInversePairs(n: int, k: int) -> int:
    mod = 10 ** 9 + 7

    if k == 0:
        return 1

    count = [1] + [0 for x in range(k)]
    for j in range(1, n):
        nxt_count = [1] + [0 for x in range(k)]
        tmp = 1
        for i in range(1, k + 1):
            tmp += count[i]
            if i >= j + 1:
                tmp -= count[i - j - 1]
            nxt_count[i] = tmp % mod
        count = nxt_count
    return count[-1]