"""
Question Source:Leetcode
Level: Medium
Topic: Tree
Solver: Tayyrov
Date: 19.04.2022
"""
from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def recoverTree(self, root: Optional[TreeNode]) -> None:
        """
        Do not return anything, modify root in-place instead.
        """
        nodes = []

        def dfs(node):
            if not node:
                return
            dfs(node.left)
            nodes.append(node)
            dfs(node.right)

        dfs(root)
        vals = sorted([node.val for node in nodes])
        for i in range(len(nodes)):
            nodes[i].val = vals[i]