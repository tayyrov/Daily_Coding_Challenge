"""
Question Source:https://leetcode.com/problems/clone-graph/
Level: Medium
Topic: Graph
Solver: Tayyrov
Date: 23.02.2022
"""
class Node:
    def __init__(self, val=0, neighbors=None):
        self.val = val
        self.neighbors = neighbors if neighbors else []


def cloneGraph(self, root: 'Node') -> 'Node':
    old_to_new = {}

    def clone(node):
        if node in old_to_new:
            return old_to_new[node]

        copy = Node(node.val)
        old_to_new[node] = copy
        for nei in node.neighbors:
            copy.neighbors.append(clone(nei))

        return copy

    return clone(root) if root else None
