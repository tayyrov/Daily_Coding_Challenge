"""
Question Source:Leetcode
Level: Medium
Topic: Tree, DFS
Solver: Tayyrov
Date: 13.05.2022
"""
from collections import deque

class Node:
    def __init__(self, val: int = 0, left: 'Node' = None, right: 'Node' = None, next: 'Node' = None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next
class Solution:
    def connect(self, root: 'Node') -> 'Node':
        if not root:
            return root

        nodes_with_levels = []

        q = deque([(root, 0)])

        while q:

            curr_node, curr_level = q.popleft()
            nodes_with_levels.append((curr_node, curr_level))
            if curr_node.left:
                q.append((curr_node.left, curr_level + 1))
            if curr_node.right:
                q.append((curr_node.right, curr_level + 1))

        ln = len(nodes_with_levels)

        for i in range(ln - 1):
            if nodes_with_levels[i][1] == nodes_with_levels[i + 1][1]:
                nodes_with_levels[i][0].next = nodes_with_levels[i + 1][0]
        return root