"""
Question Source:Leetcode
Level: Medium
Topic: Linked List
Solver: Tayyrov
Date: 22.07.2022
"""
from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def partition(self, head: Optional[ListNode], x: int) -> Optional[ListNode]:

        start_head = ListNode(0)
        start = start_head
        tail = ListNode(0)
        end = tail

        current = head

        while current:
            if current.val < x:
                start.next = ListNode(current.val)
                start = start.next
            else:
                if not end:
                    end = ListNode(current.val)
                else:
                    end.next = ListNode(current.val)
                    end = end.next
            current = current.next
        start.next = tail.next
        return start_head.next