from typing import List

class Solution:
    def findAndReplacePattern(self, words: List[str], pattern: str) -> List[str]:
        def match_pattern(word, pattern):
            word_to_pattern = {}
            pattern_to_word = {}
            
            for w, p in zip(word, pattern):
                if w not in word_to_pattern:
                    word_to_pattern[w] = p
                if p not in pattern_to_word:
                    pattern_to_word[p] = w
                if word_to_pattern[w] != p or pattern_to_word[p] != w:
                    return False
            
            return True
        
        res = []
        for word in words:
            if match_pattern(word, pattern):
                res.append(word)
        
        return res
