"""
Question Source: https://leetcode.com/problems/maximum-depth-of-binary-tree/
Level: Easy
Topic: Tree
Solver: Tayyrov
Date: 14.02.2022
"""
from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def maxDepth(root: Optional[TreeNode]) -> int:
    #         if not root:
    #             return 0
    #         q = deque([(root, 1)])

    #         while q:
    #             curr_node, curr_level = q.popleft()
    #             ans = curr_level
    #             if curr_node.left:
    #                 q.append((curr_node.left, curr_level+1))
    #             if curr_node.right:
    #                 q.append((curr_node.right, curr_level+1))
    #         return ans
    if not root:
        return 0
    return max(maxDepth(root.left), maxDepth(root.right)) + 1

"""
Time : O(N)
Space: O(h) where h is the height of the tree, in theory h can be equal to the N
"""
