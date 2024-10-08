from typing import List

class Solution:
    
    def findLongestWord(self, s: str, dictionary: List[str]) -> str:
        def is_subsequence(word, s):
            i, j = 0, 0
            while i < len(word) and j < len(s):
                if word[i] == s[j]:
                    i += 1
                j += 1
            return i == len(word)
        
        dictionary.sort(key=lambda x: (-len(x), x))
        for word in dictionary:
            if is_subsequence(word, s):
                return word
        return ""
