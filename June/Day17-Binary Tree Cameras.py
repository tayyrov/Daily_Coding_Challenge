"""
Question Source:Leetcode
Level: Hard
Topic: DP, greedy, Tree
Solver: Tayyrov
Date: 16.06.2022
"""
from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def minCameraCover(self, root: Optional[TreeNode]) -> int:
        ans = 0
        covered = {None}

        def dfs(node, par=None):
            nonlocal ans
            if node:
                dfs(node.left, node)
                dfs(node.right, node)
                if (par is None and node not in covered or
                        node.left not in covered or node.right not in covered):
                    ans += 1
                    covered.update({node, par, node.left, node.right})

        dfs(root)
        return ans

"""
Time: O(N) where N is the number of nodes
Space: O(N) due to the DFS stack 
"""
