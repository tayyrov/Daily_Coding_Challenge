"""
Question Source:Leetcode
Level: Medium
Topic: Tree
Solver: Tayyrov
Date: 15.04.2022
"""


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


from typing import Optional


def trimBST(root: Optional[TreeNode], low: int, high: int) -> Optional[TreeNode]:
    def dfs(node):
        if not node:
            return None

        node.left = dfs(node.left)
        node.right = dfs(node.right)
        # condition
        if node.val < low:
            return node.right
        elif node.val > high:
            return node.left
        else:
            return node

    return dfs(root)
