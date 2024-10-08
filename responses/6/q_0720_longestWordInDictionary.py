from typing import List

class Solution:
    def longestWord(self, words: List[str]) -> str:
        words_set = set(words)
        words.sort(key=lambda x: (-len(x), x))
        
        for word in words:
            buildable = True
            for i in range(1, len(word)):
                if word[:i] not in words_set:
                    buildable = False
                    break
            
            if buildable:
                return word
        
        return ""

    # If you have multiple solutions, add them all here as methods of the same class.
