"""
Question Source: https://leetcode.com/problems/string-to-integer-atoi/
Level: Medium
Topic: String
Solver: Tayyrov
Date: 01.14.2022
"""

def string_to_int(s: str) -> int:
    # getting rid of leading and trailing white spaces(default)
    s = s.strip()
    if not s:
        return 0
    minus = False
    if s[0] == "-":
        minus = True

    ans = 0  # initiated as 0 to deal with edge cases, because except return is 0 when no number
    MAX = 2 ** 31 - 1
    MIN = -2 ** 31
    for index, char in enumerate(s):
        if char in {"-", "+"} and index == 0:
            continue
        if char.isdigit():
            current = int(char)
            # This can be simplified if we do not assume that the current system only support 32 bit
            if (ans > MAX // 10 or ans == MAX // 10 and current > 7) and not minus:
                return MAX
            elif (-ans < MIN // 10 or ans == -MIN // 10 and current > 8) and minus:
                return MIN
            ans = ans * 10 + current
        else:
            break

    if minus:
        return -ans
    return ans


"""
Time Complexity: O(N) => due to the strip function, otherwise would be O(1) due to only looping until num gets
unsuitable for 32 bit system
Space Complexity: O(1)
"""
