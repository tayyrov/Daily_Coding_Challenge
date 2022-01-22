"""
Question Source: https://leetcode.com/problems/stone-game-iv/
Level: Hard
Topic: Dynamic Programming
Solver: Tayyrov
Date: 01.22.2022
"""

def winnerSquareGame(n: int) -> bool:
    dp = [False] * (n + 1)
    for i in range(1, n + 1):
        j = 1
        # check whether it is possible to make a next move false by subtracting one of the squares <= n, if so from
        # that point Alice can make a a move that makes the Bob to loose so mark the current point i.e "i" as a
        # winning point.
        while j * j <= i:
            if dp[i - j * j] == False:
                dp[i] = True
                break
            j += 1
        # else:
        #     dp[i] = False  # This is redundant here, as the array is already labeled False by default but for clarity
            # if Alice cannot make a move where the next one is False, then that means whatever move the alice do (
            # subtracting any of the squares) will make the next move True( winning move for Bob)

    return dp[n]


"""
Time Complexity: O(n*sqrt(N))
Space Complexity: O(N)

"""