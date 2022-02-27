"""
Question Source:Leetcode
Level: Medium
Topic: Tree
Solver: Tayyrov
Date: 27.02.2022
"""

from collections import deque
from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def widthOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0

        q = deque([(root, 0)])
        ans = 0
        while q:
            len_q = len(q)
            ans = max(ans, q[-1][1] - q[0][1] + 1)
            for i in range(len_q):
                curr, idx = q.popleft()

                if curr.left:
                    q.append((curr.left, 2 * idx))

                if curr.right:
                    q.append((curr.right, 2 * idx + 1))
        return ans
"""
Time complexity is O(n), where n is number of nodes, because we traverse our tree, using bfs. 
Space complexity is O(w), where w is the biggest number of nodes in level, because we need to keep our queue for a level.
"""