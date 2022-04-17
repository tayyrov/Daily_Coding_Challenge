"""
Question Source:Leetcode
Level: Easy
Topic: Tree
Solver: Tayyrov
Date: 17.04.2022
"""


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def increasingBST(self, root: TreeNode) -> TreeNode:
        lst = []

        def dfs(node):
            if not node:
                return
            dfs(node.left)
            lst.append(node.val)
            dfs(node.right)
            return node
        dfs(root)
        ans = TreeNode(lst[0])

        curr = ans

        for n in lst[1:]:
            curr.right = TreeNode(n)
            curr = curr.right
        return ans