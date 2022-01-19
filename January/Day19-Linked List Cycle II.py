"""
Question Source: https://leetcode.com/problems/linked-list-cycle-ii/
Level: Medium
Topic: Linked List
Solver: Tayyrov
Date: 01.19.2022
"""


# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


def detectCycle(head: ListNode):
    if not head:
        return
    slow = head
    fast = head

    while fast and fast.next:
        fast = fast.next.next
        slow = slow.next

        if fast == slow:  # means there is a cycle, if we start other pointer at the head the slower will meet
            # with that pointer at the cycle node. do math it is simple algebra
            slow2 = head
            while slow != slow2:
                slow = slow.next
                slow2 = slow2.next
            return slow

    return

"""
Time complexity = O(N)
Space Complexity = O(1)
"""