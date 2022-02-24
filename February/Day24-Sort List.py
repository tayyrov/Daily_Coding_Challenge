"""
Question Source:https://leetcode.com/problems/sort-list/
Level: Medium
Topic: Linked List
Solver: Tayyrov
Date: 24.02.2022
"""


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def sortList(head: ListNode) -> ListNode:
        vals = []
        while head:
            vals.append(head.val)
            head = head.next

        vals.sort()
        ans = ListNode(-1)

        curr = ans

        for n in vals:
            new_node = ListNode(n)
            curr.next = new_node
            curr = curr.next

        return ans.next
