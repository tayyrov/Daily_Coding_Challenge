"""
Question Source: https://leetcode.com/problems/complement-of-base-10-integer/
Level: Easy
Topic: Bitwise Operation
Solver: Tayyrov
Date: 04.01.2022
"""


# Layman's solution:

def bitwiseComplement1(N: int) -> int:
    binary = bin(N)[2:]
    bn = ""
    for i in binary:
        if i == "0":
            bn += "1"
        else:
            bn += "0"

    return int(bn, 2)


# better Solution:
def bitwiseComplement2(N: int) -> int:
    LEN = len(bin(N)[2:])
    # Largest power of 2 that covers most significant bit in N:
    largest_power_two = 2**LEN
    all_ones = largest_power_two - 1
    return all_ones - N  # ex if N==5 It is in binary == 101 and 2**3 = 8, 8 -1 = 7 which is 111 in binary and
    # 111- 101 = 010 == 2 , which is 7 - 5

def check():
    assert bitwiseComplement1(5) == 2
    assert bitwiseComplement2(5) == 2
    print("All run is OK")


check()
