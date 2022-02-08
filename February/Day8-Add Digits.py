"""
Question Source: https://leetcode.com/problems/add-digits/
Level: Easy
Topic: Stimulation
Solver: Tayyrov
Date: 08.02.2022
"""

def addDigits(num: int) -> int:

    def getDigits(num):
        digits = []

        while num:
            digits.append(num %10)
            num //= 10
        return digits
    digit_sum = sum(getDigits(num))

    while digit_sum > 9:
        digit_sum = sum(getDigits(digit_sum))

    return digit_sum