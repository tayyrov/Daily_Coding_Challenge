"""
Question Source:Leetcode
Level: Medium
Topic: BFS
Solver: Tayyrov
Date: 14.05.2022
"""

from collections import deque
from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def deepestLeavesSum(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        q = deque([(root, 0)])
        level = -1
        while q:

            node, curr_level = q.popleft()

            if curr_level != level:
                ans = node.val
                level = curr_level
            else:
                ans += node.val

            if node.left:
                q.append((node.left, curr_level + 1))
            if node.right:
                q.append((node.right, curr_level + 1))

        return ans

