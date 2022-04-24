"""
Question Source:Leetcode
Level: Medium
Topic: Hash set
Solver: Tayyrov
Date: 23.04.2022
"""


class Codec:
    def __init__(self):
        self.coded = {}

    def encode(self, longUrl: str) -> str:
        """Encodes a URL to a shortened URL.
        """
        self.coded[longUrl] = longUrl
        return self.coded[longUrl]

    def decode(self, shortUrl: str) -> str:
        """Decodes a shortened URL to its original URL.
        """
        return self.coded[shortUrl]