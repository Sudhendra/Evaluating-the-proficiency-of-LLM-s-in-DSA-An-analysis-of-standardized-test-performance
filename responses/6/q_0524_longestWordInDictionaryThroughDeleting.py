from typing import List

class Solution:
    def is_subsequence(self, s: str, word: str) -> bool:
        i, j = 0, 0
        while i < len(s) and j < len(word):
            if s[i] == word[j]:
                j += 1
            i += 1
        return j == len(word)

    def findLongestWord(self, s: str, dictionary: List[str]) -> str:
        longest_word = ''
        for word in dictionary:
            if self.is_subsequence(s, word):
                if len(word) > len(longest_word) or (len(word) == len(longest_word) and word < longest_word):
                    longest_word = word
        return longest_word
