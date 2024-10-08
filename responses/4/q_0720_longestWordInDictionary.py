from collections import defaultdict

class Solution:
    def longestWord(self, words: List[str]) -> str:
        words.sort()  # Sort the words lexicographically
        word_set = set(words)
        longest_word = ""

        for word in words:
            valid = True
            for i in range(1, len(word)):
                if word[:i] not in word_set:
                    valid = False
                    break
            if valid and len(word) > len(longest_word):
                longest_word = word

        return longest_word
