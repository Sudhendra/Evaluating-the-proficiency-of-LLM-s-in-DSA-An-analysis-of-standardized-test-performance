from typing import List

class Solution:
    def is_subsequence(self, word: str, s: str) -> bool:
        i = 0
        for c in s:
            if i < len(word) and word[i] == c:
                i += 1
        return i == len(word)

    def findLongestWord(self, s: str, dictionary: List[str]) -> str:
        dictionary.sort(key=lambda x: (-len(x), x))  # Sort by descending word length and lexicographical order
        for word in dictionary:
            if self.is_subsequence(word, s):
                return word
        return ""
