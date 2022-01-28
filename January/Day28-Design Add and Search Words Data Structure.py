"""
Question Source: https://leetcode.com/problems/design-add-and-search-words-data-structure/
Level: Medium
Topic: Trie
Solver: Tayyrov
Date: 01.28.2022
"""


class TrieNode:
    def __init__(self):
        self.children = {}
        self.end = False


class WordDictionary:

    def __init__(self):
        self.root = TrieNode()

    def addWord(self, word: str) -> None:
        curr = self.root
        for letter in word:
            if letter not in curr.children:
                curr.children[letter] = TrieNode()
            curr = curr.children[letter]
        curr.end = True

    def search(self, word: str) -> bool:

        stack = [(self.root, word)]

        while stack:

            node, w = stack.pop()

            if not w:
                if node.end:
                    return True

            elif w[0] == ".":
                # current can be any of the carcters so we add the children of children wchis is values of childen
                # for the next charcter
                for child in node.children.values():
                    stack.append((child, w[1:]))

            else:
                if w[0] in node.children:
                    stack.append((node.children[w[0]], w[1:]))
        return False

"""
Time complexity: O(M), potentially we can visit all our Trie, if we have pattern like ...... For words without ., time 
complexity will be O(h), where h is height of Trie. 
Space Complexity: O(M), M is sum of lengths of all words in our Trie. This is worst case: in practice it will be 
less than M depending on how much words are intersected. 
"""