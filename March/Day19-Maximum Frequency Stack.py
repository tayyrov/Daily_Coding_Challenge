"""
Question Source:Leetcode
Level: Hard
Topic: Stack
Solver: Tayyrov
Date: 19.03.2022
"""

class FreqStack:

    def __init__(self):
        self.map = {}
        self.mx = 0
        self.stacks = {}

    def push(self, val: int) -> None:
        val_count = self.map.get(val, 0) + 1
        self.map[val] = val_count
        if val_count > self.mx:
            self.mx = val_count
            self.stacks[val_count] = []
        self.stacks[val_count].append(val)

    def pop(self) -> int:
        res = self.stacks[self.mx].pop()
        self.map[res] -= 1

        if not self.stacks[self.mx]:
            self.mx -= 1
        return res