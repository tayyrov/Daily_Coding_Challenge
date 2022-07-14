"""
Question Source:Leetcode
Level: Medium
Topic: Tree
Solver: Tayyrov
Date: 14.07.2022
"""
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
from typing import List, Optional


class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        lookup = {n: idx for idx, n in enumerate(inorder)}
        preorder = preorder[::-1]

        def rec(start, end):
            if start > end:
                return None
            curr = preorder.pop()
            mid_idx = lookup[curr]
            root = TreeNode(curr)
            root.left = rec(start, mid_idx - 1)
            root.right = rec(mid_idx + 1, end)
            return root

        return rec(0, len(inorder) - 1)
