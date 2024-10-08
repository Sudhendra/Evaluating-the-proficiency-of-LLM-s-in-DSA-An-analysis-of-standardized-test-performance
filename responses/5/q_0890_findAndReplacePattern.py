from typing import List

class Solution:
    def findAndReplacePattern(self, words: List[str], pattern: str) -> List[str]:
        def is_match(word, pattern):
            mapping_wp = {}
            mapping_pw = {}
            
            for w, p in zip(word, pattern):
                if w not in mapping_wp:
                    mapping_wp[w] = p
                if p not in mapping_pw:
                    mapping_pw[p] = w
                if mapping_wp[w] != p or mapping_pw[p] != w:
                    return False
            return True
        
        result = []
        for word in words:
            if is_match(word, pattern):
                result.append(word)
        
        return result
