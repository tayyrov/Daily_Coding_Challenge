"""
Question Source:Leetcode
Level: Medium
Topic: Set, Math
Solver: Tayyrov
Date: 31.05.2022
"""


def hasAllCodes(s: str, k: int) -> bool:
    ln = len(s)

    def solve(n):
        st = set()
        aim = 2 ** n

        for i in range(ln - n + 1):
            st.add(s[i:i + n])

            if len(st) == aim:
                return True
        # print(st, n)
        return False

    for i in range(1, k + 1):
        if not solve(i):
            return False

    return True