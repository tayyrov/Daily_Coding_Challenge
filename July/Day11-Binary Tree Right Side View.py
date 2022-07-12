"""
Question Source:Leetcode
Level: Medium
Topic: Tree
Solver: Tayyrov
Date: 11.07.2022
"""
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
from typing import Optional, List


class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        if not root:
            return []
        last_level = dict()

        q = deque([(root, 0)])

        while q:
            curr, level = q.popleft()
            last_level[level] = curr.val
            if curr.left:
                q.append((curr.left, level +1))
            if curr.right:
                q.append((curr.right, level +1))

        return list(last_level.values())