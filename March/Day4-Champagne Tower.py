"""
Question Source:Leetcode
Level: Medium
Topic: Stimulation, DP
Solver: Tayyrov
Date: 04.03.2022
"""


def champagneTower(poured: int, query_row: int, query_glass: int) -> float:
    curr = [poured]

    for _ in range(query_row):
        temp = [0] * (len(curr) + 1)  # next line will have one more cups than the previous one
        for i in range(len(curr)):
            excess = curr[i] - 1  # capacity of the each cup is one so anything extra will be moving down
            if excess > 0:
                temp[
                    i] += excess / 2  # half of each excess amount will ewually go left and right until one level below lef/right is full
                temp[i + 1] += excess / 2

        curr = temp  # move to the next row

    return min(1, curr[query_glass])  # a cup can have a maximum of 1
