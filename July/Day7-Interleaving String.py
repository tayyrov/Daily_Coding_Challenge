"""
Question Source:Leetcode
Level: Medium
Topic: DP
Solver: Tayyrov
Date: 07.07.2022
"""


def isInterleave(s1: str, s2: str, s3: str) -> bool:
    if len(s3) != len(s1) + len(s2):
        return False
    seen = dict()

    def dp(s1_idx, s2_idx):
        s3_idx = s1_idx + s2_idx
        if s3_idx == len(s3):
            return True
        if (s1_idx, s2_idx) in seen:
            return seen[(s1_idx, s2_idx)]

        op1 = s1_idx < len(s1) and s1[s1_idx] == s3[s3_idx] and dp(s1_idx + 1, s2_idx)
        op2 = s2_idx < len(s2) and s2[s2_idx] == s3[s3_idx] and dp(s1_idx, s2_idx + 1)
        seen[(s1_idx, s2_idx)] = op1 or op2
        return seen[(s1_idx, s2_idx)]

    return dp(0, 0)