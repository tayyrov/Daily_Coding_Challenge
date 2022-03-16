"""
Question Source:Leetcode
Level: Medium
Topic: Stack
Solver: Tayyrov
Date: 14.03.2022
"""


def simplifyPath(path: str) -> str:
    path = path.split("/")
    ans = []
    for p in path:
        if p == "." or p == "":
            continue
        elif p == "..":
            if ans:
                ans.pop()
        else:
            ans.append(p)
    return "/" + "/".join(ans)
