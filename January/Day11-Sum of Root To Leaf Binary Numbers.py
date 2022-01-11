"""
Question Source: https://leetcode.com/problems/sum-of-root-to-leaf-binary-numbers/
Level: Easy
Topic: Tree
Solver: Tayyrov
Date: 01.11.2022
"""
from typing import *


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def sumRootToLeaf(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        total = 0

        stack = [(root, str(root.val))]

        while stack:
            node, path = stack.pop()

            if node.left == node.right:  # means it is leaf so we can convert the pth into int and add to the total
                total += int(path, 2)

            if node.left:
                stack.append((node.left, path + str(node.left.val)))

            if node.right:
                stack.append((node.right, path + str(node.right.val)))

        return total
