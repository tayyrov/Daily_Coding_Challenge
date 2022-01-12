"""
Question Source: https://leetcode.com/problems/insert-into-a-binary-search-tree/
Level: Medium
Topic: Binary Search Tree
Solver: Tayyrov
Date: 01.12.2022
"""

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


from typing import *


class Solution:
    def insertIntoBST(self, root: Optional[TreeNode], val: int) -> Optional[TreeNode]:

        new_node = TreeNode(val)

        if not root:
            return new_node
        current = root
        while True:
            if current.val > val:  # we should go left if possible if not we insert the node
                if current.left:
                    current = current.left
                else:
                    current.left = new_node
                    break
            else:  # means current.val < val so move right if possible
                if current.right:
                    current = current.right
                else:
                    current.right = new_node
                    break
        return root
