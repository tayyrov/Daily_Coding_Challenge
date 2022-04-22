"""
Question Source:Leetcode
Level: Easy
Topic: Hash set
Solver: Tayyrov
Date: 22.04.2022
"""

class MyHashMap:

    def __init__(self):
        self.hash = [None] * 10**7

    def put(self, key: int, value: int) -> None:
        self.hash[key] = value

    def get(self, key: int) -> int:
        if self.hash[key] != None:
            return self.hash[key]
        return -1

    def remove(self, key: int) -> None:
        self.hash[key] = None



