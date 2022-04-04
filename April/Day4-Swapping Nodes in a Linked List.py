"""
Question Source:Leetcode
Level: Medium
Topic: Array
Solver: Tayyrov
Date: 04.04.2022
"""
from typing import List, Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def swapNodes(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:

        curr = head
        ln = 0
        while curr:
            ln += 1
            curr = curr.next

        curr = head
        index = 1
        sec_k = ln - k + 1
        while curr:
            if k == index:
                first = curr.val
            if index == sec_k:
                second = curr.val
            index += 1
            curr = curr.next

        curr = head
        index = 1
        while curr:
            if k == index:
                curr.val = second
            if index == sec_k:
                curr.val = first
            index += 1
            curr = curr.next
        return head

"""
Time complexity: O(N)
Space complexity: O(1)
"""