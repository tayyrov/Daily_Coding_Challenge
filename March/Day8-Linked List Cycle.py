"""
Question Source:Leetcode
Level: Easy
Topic: Linked List
Solver: Tayyrov
Date: 08.03.2022
"""

class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


def hasCycle(head: ListNode) -> bool:
    if not head:
        return False
    slow = head
    fast = head

    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next
        if slow == fast:
            return True

    return False
