from typing import List

class TrieNode:
    def __init__(self):
        self.children = {}
        self.is_end = False

class Solution:
    def findAllConcatenatedWordsInADict(self, words: List[str]) -> List[str]:
        def build_trie():
            root = TrieNode()
            for word in words:
                if not word:
                    continue
                node = root
                for char in word:
                    if char not in node.children:
                        node.children[char] = TrieNode()
                    node = node.children[char]
                node.is_end = True
            return root

        def dfs(word, index, count):
            node = trie
            for i in range(index, len(word)):
                char = word[i]
                if char not in node.children:
                    return False
                node = node.children[char]
                if node.is_end:
                    if i == len(word) - 1:
                        return count >= 1
                    if dfs(word, i + 1, count + 1):
                        return True
            return False

        trie = build_trie()
        concatenated_words = []
        for word in words:
            if not word:
                continue
            if dfs(word, 0, 0):
                concatenated_words.append(word)
        return concatenated_words
