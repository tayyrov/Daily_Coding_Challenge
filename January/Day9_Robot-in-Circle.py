"""
Question Source: https://leetcode.com/problems/robot-bounded-in-circle/
Level: Medium
Topic: Math
Solver: Tayyrov
Date: 01.09.2022
"""
from typing import *


def isRobotBounded(instructions: str) -> bool:
    # starting position
    x, y = (0, 0)

    # initially facing
    dx, dy = (0, 1)

    for command in instructions:
        if command == "L":
            dx, dy = dy, -dx
        elif command == "R":
            dx, dy = -dy, dx
        elif command == "G":
            x, y = x + dx, y + dy

    # it the final position is at the starting position or face is looking than the initial side then there is cycle
    # for example lets say initially it is looking up but if is facing left or right after maximum of four cicrle it
    # will come to the same position
    return (x, y) == (0, 0) or (dx, dy) != (0, 1)


def check():
    assert isRobotBounded("GGLLGG") == True
    assert isRobotBounded("GG") == False

    print("All runs are OK")
check()
