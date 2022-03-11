"""
Question Source:Leetcode
Level: Medium
Topic: Linked List
Solver: Tayyrov
Date: 10.03.2022
"""
from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def addTwoNumbers(l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:

        ans = prev = ListNode(0)

        left_over = 0
        while l1 or l2 or left_over:
            if l1:
                num1 = l1.val
                l1 = l1.next
            else:
                num1 = 0
            if l2:
                num2 = l2.val
                l2 = l2.next
            else:
                num2 = 0

            left_over, curr_digit = divmod(num1 + num2 + left_over, 10)
            prev.next = ListNode(curr_digit)
            prev = prev.next
        return ans.next