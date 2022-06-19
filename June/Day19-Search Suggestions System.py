"""
Question Source:Leetcode
Level: Medium
Topic: Two pointer
Solver: Tayyrov
Date: 19.06.2022
"""

from typing import List


def suggestedProducts(products: List[str], searchWord: str) -> List[List[str]]:
    products.sort()

    left = 0
    right = len(products) - 1
    ans = []
    for i, char in enumerate(searchWord):

        while left <= right and (i >= len(products[left]) or products[left][i] != char):
            left += 1
        while left <= right and (i >= len(products[right]) or products[right][i] != char):
            right -= 1

        window = right - left + 1

        temp = []

        for j in range(min(3, window)):
            temp.append(products[left + j])

        ans.append(temp)
    return ans

"""
Time: nlogn + N*len(searchWord) where N is the len of products
Space: O(1)
"""