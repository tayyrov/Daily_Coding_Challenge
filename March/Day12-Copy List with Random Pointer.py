"""
Question Source:Leetcode
Level: Medium
Topic: Linked List
Solver: Tayyrov
Date: 12.03.2022
"""


class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random

class Solution:
    def copyRandomList(head: 'Node') -> 'Node':

        # return deepcopy(head) # cheat solution

        if not head:
            return

        nodes = dict()
        curr = head

        while curr:
            nodes[curr] = Node(curr.val)
            curr = curr.next

        curr = head

        while curr:
            if curr.random:
                nodes[curr].random = nodes[curr.random]

            if curr.next:
                nodes[curr].next = nodes[curr.next]
            curr = curr.next

        return nodes[head]