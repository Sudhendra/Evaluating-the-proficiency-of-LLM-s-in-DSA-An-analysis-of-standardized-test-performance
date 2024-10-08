from typing import List

class Solution:
    def findLongestWord(self, s: str, dictionary: List[str]) -> str:
        def is_subsequence(word, s):
            i = 0
            for c in s:
                if i < len(word) and word[i] == c:
                    i += 1
            return i == len(word)
        
        dictionary.sort(key=lambda x: (-len(x), x))
        for word in dictionary:
            if is_subsequence(word, s):
                return word
        return ""