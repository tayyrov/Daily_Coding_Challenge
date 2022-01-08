"""
Question Source: https://leetcode.com/problems/linked-list-random-node/
Level: Medium
Topic: Linked List
Solver: Tayyrov
Date: 01.07.2022
"""
from typing import *
import random


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:

    def __init__(self, head: Optional[ListNode]):
        self.values = []
        current = head
        while current:
            self.values.append(current.val)
            current = current.next

    def getRandom(self) -> int:
        return random.choice(self.values)
