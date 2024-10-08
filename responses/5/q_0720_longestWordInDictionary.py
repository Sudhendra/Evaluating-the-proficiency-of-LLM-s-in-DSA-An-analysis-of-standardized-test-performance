from typing import List

class Solution:
    def longestWord(self, words: List[str]) -> str:
        words = sorted(words)  # Sort words lexicographically
        words_set = set(words)  # Convert words to a set for efficient lookup
        longest_word = ""

        for word in words:
            valid = True
            for i in range(1, len(word)):  # Check if all prefixes of the word are in the words set
                if word[:i] not in words_set:
                    valid = False
                    break
            if valid and len(word) > len(longest_word):
                longest_word = word
            elif valid and len(word) == len(longest_word) and word < longest_word:  # Update if lexicographically smaller
                longest_word = word

        return longest_word
