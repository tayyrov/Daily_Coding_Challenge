"""
Question Source:Leetcode
Level: String
Topic: String
Solver: Tayyrov
Date: 25.02.2022
"""


def compareVersion(version1: str, version2: str) -> int:
    v1 = list(map(int, version1.split(".")))
    v2 = list(map(int, version2.split(".")))

    dif = abs(len(v1) - len(v2))
    extra = [0] * dif
    if len(v1) < len(v2):
        v1 += extra
    else:
        v2 += extra

    for n1, n2 in zip(v1, v2):
        if n1 > n2:
            return 1
        elif n2 > n1:
            return -1
    return 0
