from typing import List

class Solution:
    def findAndReplacePattern(self, words: List[str], pattern: str) -> List[str]:
        def is_isomorphic(word, pattern):
            mapping_word = {}
            mapping_pattern = {}
            for w, p in zip(word, pattern):
                if w not in mapping_word:
                    mapping_word[w] = p
                if p not in mapping_pattern:
                    mapping_pattern[p] = w
                if mapping_word[w] != p or mapping_pattern[p] != w:
                    return False
            return True

        result = []
        for word in words:
            if is_isomorphic(word, pattern):
                result.append(word)
        return result
