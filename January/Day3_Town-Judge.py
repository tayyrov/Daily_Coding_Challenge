"""
Question Source: https://leetcode.com/problems/find-the-town-judge/
Level: Easy
Topic: Graph
Solver: Tayyrov
Date: 03.01.2022
"""
from collections import defaultdict


def findJudge_solution1(trust, n) -> int:
    trustees = defaultdict(set)  # as the values are unique list as a value type can be used too

    trusters = set()  # these can not be a judge
    for person, judge in trust:
        trustees[judge].add(person)
        trusters.add(person)

    for key, val in trustees.items():
        if key not in trusters and len(val) == n - 1:  # contains all except itself
            return key  # Logically there can be only one person who has N-1 votes and trusts nobody, so we can
            # return whenever we find one
    # edge_case: when we have only one person and empty trust list => means everyone except itself trusts him
    if n == 1 and trust == []:
        return 1
    return -1


# alternative solution using counting
def findJudge_solution2(trust, n) -> int:
    frequency_table = [0] * (n)

    for trusting, being_trusted in trust:
        frequency_table[trusting - 1] -= 1
        frequency_table[being_trusted - 1] += 1

    for idx in range(n):
        if frequency_table[idx] == n - 1:  # if someone trusts anyone it would have less thant N-1 trustees as
            # trusting someone is -1. similarly is someone doesnt trust you, then again it is not possible to get N-1
            # value (-1 comes because judge doesnt trust himself)
            return idx + 1

    return -1
