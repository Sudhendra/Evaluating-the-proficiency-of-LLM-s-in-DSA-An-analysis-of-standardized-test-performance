from typing import List

class Solution:
    def findAndReplacePattern(self, words: List[str], pattern: str) -> List[str]:
        def match_pattern(word, pattern):
            if len(word) != len(pattern):
                return False

            word_to_pattern = {}
            pattern_to_word = {}
            for w, p in zip(word, pattern):
                if w not in word_to_pattern and p not in pattern_to_word:
                    word_to_pattern[w] = p
                    pattern_to_word[p] = w
                elif word_to_pattern.get(w) != p or pattern_to_word.get(p) != w:
                    return False
            return True

        return [word for word in words if match_pattern(word, pattern)]