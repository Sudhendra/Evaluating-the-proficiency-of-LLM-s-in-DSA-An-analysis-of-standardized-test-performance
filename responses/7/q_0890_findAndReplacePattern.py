from typing import List

class Solution:
    def findAndReplacePattern(self, words: List[str], pattern: str) -> List[str]:
        def match_pattern(word, pattern):
            if len(word) != len(pattern):
                return False
            word_to_pattern = {}
            pattern_to_word = {}
            for w, p in zip(word, pattern):
                if (w in word_to_pattern and word_to_pattern[w] != p) or (p in pattern_to_word and pattern_to_word[p] != w):
                    return False
                else:
                    word_to_pattern[w] = p
                    pattern_to_word[p] = w
            return True

        res = []
        for word in words:
            if match_pattern(word, pattern):
                res.append(word)
        return res
