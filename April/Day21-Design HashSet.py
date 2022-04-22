"""
Question Source:Leetcode
Level: Easy
Topic: Hash set
Solver: Tayyrov
Date: 21.04.2022
"""
class MyHashSet:

    def __init__(self):
        self.st = [None] *(10 **6+1)

    def add(self, key: int) -> None:
        self.st[key] = key

    def remove(self, key: int) -> None:
        self.st[key] = None

    def contains(self, key: int) -> bool:
        return self.st[key] != None
