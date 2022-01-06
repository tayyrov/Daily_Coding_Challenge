"""
Question Source: https://leetcode.com/problems/car-pooling/
Level: Medium
Topic: Sorting, stimulation
Solver: Tayyrov
Date: 01.06.2022
"""
from typing import *


def carPooling(trips: List[List[int]], capacity: int) -> bool:
    passenger_logistics = []

    for nums_pass, add, remove in trips:
        # minus comes before plus, meaning after sorting first we remove then we add.
        passenger_logistics.append((add, nums_pass))
        passenger_logistics.append((remove, -nums_pass))

    passenger_logistics.sort()
    # print(passenger_logistics)   [[2,1,5],[3,5,7]] => [(1, 2), (5, -2), (5, 3), (7, -3)]
    current_people = 0
    for action, people in passenger_logistics:
        current_people += people

        if current_people > capacity:
            return False

    return True


def check():
    assert carPooling([[2, 1, 5], [3, 3, 7]], 4) == False
    assert carPooling([[2, 1, 5], [3, 3, 7]], 5) == True
    print("All runs are OK")


check()
