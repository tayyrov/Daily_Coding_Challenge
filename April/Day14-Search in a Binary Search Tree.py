"""
Question Source:Leetcode
Level: Easy
Topic: Tree
Solver: Tayyrov
Date: 14.04.2022
"""


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def searchBST(self, root: TreeNode, val: int) -> TreeNode:
        if not root:
            return None
        if root.val == val:
            return root
        if root.val > val:
            return self.searchBST(root.left, val)
        else:
            return self.searchBST(root.right, val)

"""
Time complexity: O(logN)
Space complexity: O(logN) -> Due to the stack
"""
