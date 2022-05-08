"""
Question Source:Leetcode
Level: Medium
Topic: Recursion
Solver: Tayyrov
Date: 08.05.2022
"""


# """
# This is the interface that allows for creating nested lists.
# You should not implement it, or speculate about its implementation
# """
class NestedInteger(object):
    def isInteger(self) -> bool:
        """
       @return True if this NestedInteger holds a single integer, rather than a nested list.
       """

    def getInteger(self) -> int:
        """
       @return the single integer that this NestedInteger holds, if it holds a single integer
       Return None if this NestedInteger holds a nested list
       """

    def getList(self) -> [NestedInteger]:
        """
       @return the nested list that this NestedInteger holds, if it holds a nested list
       Return None if this NestedInteger holds a single integer
       """


class NestedIterator:
    def __init__(self, nestedList: [NestedInteger]):
        def flatten(lst):
            temp = []
            for num in lst:
                if num.isInteger():
                    temp.append(num.getInteger())
                else:
                    temp.extend(flatten(num.getList()))
            return temp

        self.n = flatten(nestedList)

    def next(self) -> int:
        return self.n.pop(0)

    def hasNext(self) -> bool:
        return self.n

# Your NestedIterator object will be instantiated and called as such:
# i, v = NestedIterator(nestedList), []
# while i.hasNext(): v.append(i.next())
