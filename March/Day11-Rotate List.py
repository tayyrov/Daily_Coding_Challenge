"""
Question Source:Leetcode
Level: Medium
Topic: Linked List
Solver: Tayyrov
Date: 11.03.2022
"""

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


def rotateRight(head: ListNode, k: int) -> ListNode:
    if not head:
        return
    ln = 0
    curr = head
    while curr:
        ln += 1
        curr = curr.next

    k %= ln
    if k == 0:
        return head

    offset = ln - k

    curr = head

    while curr:
        offset -= 1
        if offset == 0:
            new_head = curr.next
            # we break the chain
            curr.next = None
            break
        curr = curr.next

    curr = new_head

    while curr.next:
        curr = curr.next

    curr.next = head

    return new_head
