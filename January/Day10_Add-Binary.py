"""
Question Source: https://leetcode.com/problems/add-binary/
Level: Easy
Topic: Bit Manipulation
Solver: Tayyrov
Date: 01.10.2022
"""


def addBinary(a: str, b: str) -> str:
    carry = 0
    a_pointer = len(a) - 1
    b_pointer = len(b) - 1
    ans = ""
    while a_pointer >= 0 or b_pointer >= 0 or carry:
        temp = carry
        if a_pointer >= 0:
            temp += int(a[a_pointer])
            a_pointer -= 1
        if b_pointer >= 0:
            temp += int(b[b_pointer])
            b_pointer -= 1

        carry, remainder = divmod(temp, 2)
        ans += str(remainder)

    return ans[::-1]


def Solution2(a: str, b: str) -> str:
    return bin(int(a, 2) + int(b, 2))[2:]


def check():
    assert addBinary("11", "1") == "100"
    assert addBinary("1010", "1011") == "10101"
    print("All run is OK")


check()
