from typing import List

class TrieNode:
    def __init__(self):
        self.children = {}

class Solution:
    def minimumLengthEncoding(self, words: List[str]) -> int:
        def insert_word(root, word):
            node = root
            is_new_word = False
            for char in reversed(word):
                if char not in node.children:
                    is_new_word = True
                    node.children[char] = TrieNode()
                node = node.children[char]
            return is_new_word

        root = TrieNode()
        words = sorted(words, key=len, reverse=True)
        encoding_length = 0
        for word in words:
            if insert_word(root, word):
                encoding_length += len(word) + 1
        return encoding_length

# Example usage:
# solution = Solution()
# print(solution.minimumLengthEncoding(["time", "me", "bell"]))  # Output: 10
# print(solution.minimumLengthEncoding(["t"]))  # Output: 2
