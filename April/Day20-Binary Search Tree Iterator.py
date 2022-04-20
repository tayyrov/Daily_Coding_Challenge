"""
Question Source:Leetcode
Level: Medium
Topic: Tree
Solver: Tayyrov
Date: 20.04.2022
"""

from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class BSTIterator:
    # arr = []
    def __init__(self, root: Optional[TreeNode]):
        self.arr = []
        self.idx = 0
        def inorder(root):
            if root:
                inorder(root.left)
                self.arr.append(root.val)
                inorder(root.right)
        inorder(root)
    def next(self) -> int:
        ind = self.idx
        self.idx += 1
        return self.arr[ind]

    def hasNext(self) -> bool:
        return len(self.arr) > self.idx