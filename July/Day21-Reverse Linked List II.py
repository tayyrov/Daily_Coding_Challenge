"""
Question Source:Leetcode
Level: Medium
Topic: Linked List
Solver: Tayyrov
Date: 21.07.2022
"""
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


from typing import Optional


class Solution:
    def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:

        vals = []
        nodes = []

        current = head
        counter = 0

        while current:
            counter += 1

            if left <= counter <= right:
                nodes.append(current)
                vals.append(current.val)

            current = current.next
        for node, n in zip(nodes, vals[::-1]):
            node.val = n

        return head
