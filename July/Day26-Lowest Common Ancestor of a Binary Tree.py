"""
Question Source:Leetcode
Level: Medium
Topic: Tree
Solver: Tayyrov
Date: 26.07.2022
"""


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        global ans
        if not root:
            return None

        stack = [(root, [root])]

        path1 = None

        while stack:
            node, path = stack.pop()
            if node == p or node == q:
                if path1:
                    path = set(path)
                    for n in path1:
                        if n in path:
                            ans = n
                    return ans
                path1 = path

            if node.left:
                stack.append((node.left, path + [node.left]))
            if node.right:
                stack.append((node.right, path + [node.right]))