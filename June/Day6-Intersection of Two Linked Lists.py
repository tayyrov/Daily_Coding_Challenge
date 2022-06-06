"""
Question Source:Leetcode
Level: Easy
Topic: Linked List
Solver: Tayyrov
Date: 06.06.2022
"""


class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> ListNode:
        pointer_A = headA
        pointer_B = headB

        while pointer_A != pointer_B:
            if pointer_A is None:
                pointer_A = headB
            else:
                pointer_A = pointer_A.next
            if pointer_B is None:
                pointer_B = headA
            else:
                pointer_B = pointer_B.next

        return pointer_A