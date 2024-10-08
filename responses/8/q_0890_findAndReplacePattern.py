from typing import List

class Solution:
    def findAndReplacePattern(self, words: List[str], pattern: str) -> List[str]:
        def match_pattern(word, pattern):
            if len(word) != len(pattern):
                return False
            mapping = {}
            reverse_mapping = {}
            for w, p in zip(word, pattern):
                if w not in mapping:
                    mapping[w] = p
                if p not in reverse_mapping:
                    reverse_mapping[p] = w
                if mapping[w] != p or reverse_mapping[p] != w:
                    return False
            return True
        
        results = []
        for word in words:
            if match_pattern(word, pattern):
                results.append(word)
        
        return results
