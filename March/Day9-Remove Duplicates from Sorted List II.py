"""
Question Source:Leetcode
Level: Medium
Topic: Linked List
Solver: Tayyrov
Date: 09.03.2022
"""
from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def deleteDuplicates(head: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode(1)
        dummy.next = head
        curr = head
        prev = dummy
        while curr:
            entered = False
            while curr.next and curr.next.val == curr.val:
                curr.next = curr.next.next
                entered = True

            if entered:
                prev.next = curr.next
            else:
                prev = curr
            curr = curr.next

        return dummy.next