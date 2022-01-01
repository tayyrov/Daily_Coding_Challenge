"""
Question Source: https://leetcode.com/problems/burst-balloons/
Level: Hard
Topic: Dynamic programming & Divide-and-Conquer
Solver: Tayyrov
Date: 01.01.2022
"""


def maxCoins(nums):
    # to deal with edge cases lets add 1 to the both sides of array. These ones never burst
    nums = [1] + nums + [1]
    ln = len(nums)

    dp_array = [[0] * ln for _ in range(ln)]

    for window_size in range(1, ln):
        for left in range(ln - window_size):
            right = left + window_size

            # now lets calculate what is the best score within this range i.e. left to right not including left and
            # right themselves
            for chosen_idx in range(left + 1,
                                    right):  # left and right indices not burst but used for calculation.
                # chosen_idx is the one that burst last so at that moment it will have left on the left side and
                # right on the right side as an adjacent
                current = dp_array[left][chosen_idx] + nums[left] * nums[chosen_idx] * nums[right] + \
                          dp_array[chosen_idx][right]
                dp_array[left][right] = max(dp_array[left][right], current)
        print(dp_array)
    return dp_array[0][ln - 1]

## Below is the alternative top down uproaching usng memoziation, which has teh same running time O(N^3):
#         cached = defaultdict()

#         def dp_top_down(left, right):
#             if left > right:
#                 return 0
#             if (left, right) in cached:
#                 return cached[(left, right)]
#             cached[(left, right)] = 0
#             for i in range(left, right+1):
#                 #i chosen as a last to burst
#                 coins = nums[left-1] * nums[i] * nums[right+1]
#                 #lets addd left and right subseqeunces:
#                 coins += dp_top_down(left, i-1) + dp_top_down(i+1, right)

#                 cached[(left, right)] = max(cached[(left, right)], coins)
#             return dp_top_down(left, right)
