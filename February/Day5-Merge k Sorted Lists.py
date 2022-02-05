"""
Question Source: https://leetcode.com/problems/merge-k-sorted-lists/
Level: Hard
Topic: Linked List
Solver: Tayyrov
Date: 05.02.2022
"""
from typing import *

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        if not lists:
            return None
        while len(lists) > 1:
            merged = []
            for i in range(0, len(lists), 2):
                lst1 = lists[i]
                lst2 = lists[i + 1] if i + 1 < len(lists) else None
                merged.append(self.merge(lst1, lst2))

            lists = merged

        return lists[0]

    def merge(self, lst1, lst2):
        dummy = ListNode(-1)

        curr = dummy

        while lst1 and lst2:

            if lst1.val < lst2.val:
                curr.next = lst1
                lst1 = lst1.next
            else:
                curr.next = lst2
                lst2 = lst2.next
            curr = curr.next

        if lst1:
            curr.next = lst1
        if lst2:
            curr.next = lst2

        return dummy.next

"""
Time : O(NLogK) where N is the total number of nodes (i.e. all members of list of lists) and k is number of list
is lists
Space: O(N) 
 """