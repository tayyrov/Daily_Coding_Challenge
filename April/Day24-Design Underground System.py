"""
Question Source:Leetcode
Level: Medium
Topic: Hash set
Solver: Tayyrov
Date: 24.04.2022
"""

class UndergroundSystem:

    def __init__(self):
        self.arrive = {}
        self.path = {}

    def checkIn(self, id: int, stationName: str, t: int) -> None:
        self.arrive[id] = (stationName, t)

    def checkOut(self, id: int, stationName: str, t: int) -> None:
        getin = self.arrive[id]
        del self.arrive[id]
        time = t - getin[1]
        key = (getin[0], stationName, id)
        self.path[key] = time

    def getAverageTime(self, startStation: str, endStation: str) -> float:
        key = (startStation, endStation)
        ans = 0
        cnt = 0
        for k, val in self.path.items():
            if k[:2] == key:
                ans += val
                cnt += 1
        return ans / cnt