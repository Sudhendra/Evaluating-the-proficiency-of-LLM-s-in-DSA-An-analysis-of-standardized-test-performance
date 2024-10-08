from typing import List

class Solution:
    def findAndReplacePattern(self, words: List[str], pattern: str) -> List[str]:
        def match_pattern(word, pattern):
            if len(word) != len(pattern):
                return False

            word_to_pattern = {}
            pattern_to_word = {}
            for i in range(len(word)):
                w = word[i]
                p = pattern[i]
                if w not in word_to_pattern and p not in pattern_to_word:
                    word_to_pattern[w] = p
                    pattern_to_word[p] = w
                elif w in word_to_pattern and p in pattern_to_word:
                    if word_to_pattern[w] != p or pattern_to_word[p] != w:
                        return False
                else:
                    return False
            return True
        
        res = []
        for word in words:
            if match_pattern(word, pattern):
                res.append(word)
        
        return res