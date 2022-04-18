"""
Question Source:Leetcode
Level: Medium
Topic: Tree
Solver: Tayyrov
Date: 18.04.2022
"""


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
from typing import Optional


class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        stack = []

        while stack or root:
            while root:  # go all the way down left
                stack.append(root)
                root = root.left
            curr = stack.pop()  # this the current samplles since the last appended left
            k -= 1

            if k == 0:
                return curr.val
            root = curr.right  # lets explore the right