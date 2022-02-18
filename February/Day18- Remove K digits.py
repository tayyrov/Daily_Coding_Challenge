"""
Question Source: https://leetcode.com/problems/remove-k-digits/
Level: Medium
Topic: Monotonic Stack
Solver: Tayyrov
Date: 18.02.2022
"""


def removeKdigits(num: str, k: int) -> str:
    ans = []

    for n in num:
        while ans and ans[-1] > n and k > 0:
            ans.pop()
            k -= 1
        ans.append(n)

    while k > 0:
        ans.pop()
        k -= 1
    final_ans = "".join(ans).lstrip("0")
    return final_ans if final_ans else "0"


"""
Time: O(N)
Space: O(N)
"""
