"""
Question Source: https://leetcode.com/problems/swap-nodes-in-pairs/
Level: Medium
Topic: Linked List
Solver: Tayyrov
Date: 16.02.2022
"""

from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


def swapPairs(head: Optional[ListNode]) -> Optional[ListNode]:
    # head mighnot b th2 same head after the chnages so lets carete dummy node
    #         dummy = ListNode("dummy")
    #         dummy.next = head

    #         curr = dummy.next
    #         prev = dummy
    #         while curr and curr.next:
    #             first = curr
    #             second = curr.next
    #             prev.next = second
    #             first.next = second.next
    #             second.next= first
    #             prev = curr
    #             curr = curr.next
    #         return dummy.next
    # Solution 2 recursive:
    if not head or not head.next:
        return head
    # swap:
    new_head = head.next.next
    head, head.next = head.next, head
    head.next.next = swapPairs(new_head)
    return head

"""
Time: O(N)
Space: O(1)
"""
