"""
Question Source:Leetcode
Level: Medium
Topic: DFS
Solver: Tayyrov
Date: 17.05.2022
"""


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def getTargetCopy(self, original: TreeNode, cloned: TreeNode, target: TreeNode) -> TreeNode:
        stack = [cloned]

        while stack:
            curr = stack.pop()
            if curr.val == target.val:
                return curr

            if curr.left:
                stack.append(curr.left)

            if curr.right:
                stack.append(curr.right)