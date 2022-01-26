"""
Question Source: https://leetcode.com/problems/all-elements-in-two-binary-search-trees/
Level: Medium
Topic: BST
Solver: Tayyrov
Date: 01.26.2022
"""
from typing import *

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def getAllElements(self, root1: TreeNode, root2: TreeNode) -> List[int]:
        # we do in-order traversal so that the output is sorted, then they can be merged without sorting
        def solve(root, lst):
            if not root:
                return
            solve(root.left, lst)
            lst.append(root.val)
            solve(root.right, lst)

        lst1 = []
        solve(root1, lst1)

        lst2 = []
        solve(root2, lst2)

        ans = []
        i = 0
        j = 0
        while i < len(lst1) and j < len(lst2):
            if lst1[i] <= lst2[j]:
                ans.append(lst1[i])
                i += 1
            else:
                ans.append(lst2[j])
                j += 1

        while i < len(lst1):
            ans.append(lst1[i])
            i += 1

        while j < len(lst2):
            ans.append(lst2[j])
            j += 1
        return ans


"""
Time: O(N+M)
Space: O(N+M)
"""