"""
Question Source:Leetcode
Level: Easy
Topic: Linked List
Solver: Tayyrov
Date: 07.03.2022
"""


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


def mergeTwoLists(l1: ListNode, l2: ListNode) -> ListNode:
    root = ans = ListNode(0)

    while l1 and l2:
        if l1.val < l2.val:
            ans.next = ListNode(l1.val)
            l1 = l1.next
        else:
            ans.next = ListNode(l2.val)
            l2 = l2.next
        ans = ans.next
    if l1:
        ans.next = l1
    else:
        ans.next = l2

    return root.next

