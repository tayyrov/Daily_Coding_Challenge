"""
Question Source:Leetcode
Level: Medium
Topic: Iterator
Solver: Tayyrov
Date: 25.04.2022
"""

class PeekingIterator:
    def __init__(self, iterator):
        """
        Initialize your data structure here.
        :type iterator: Iterator
        """
        self.iterator = iterator
        self.pointer = self.iterator.next() if self.iterator.hasNext() else None

    def peek(self):
        """
        Returns the next element in the iteration without advancing the iterator.
        :rtype: int
        """
        return self.pointer

    def next(self):
        """
        :rtype: int
        """
        ans = self.pointer
        self.pointer = self.iterator.next() if self.iterator.hasNext() else None
        return ans

    def hasNext(self):
        """
        :rtype: bool
        """
        return self.pointer is not None