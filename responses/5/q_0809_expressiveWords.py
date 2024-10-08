from typing import List

class Solution:
    def expressiveWords(self, s: str, words: List[str]) -> int:
        def is_stretchy(word: str) -> bool:
            i, j, m, n = 0, 0, len(s), len(word)
            
            while i < m and j < n:
                if s[i] != word[j]:
                    return False
                
                len_s = 1
                len_word = 1
                
                while i + 1 < m and s[i + 1] == s[i]:
                    i += 1
                    len_s += 1
                
                while j + 1 < n and word[j + 1] == word[j]:
                    j += 1
                    len_word += 1
                
                if len_s < 3 and len_s != len_word:
                    return False
                
                if len_s < len_word:
                    return False
                
                i += 1
                j += 1
            
            return i == m and j == n
        
        count = 0
        for word in words:
            if is_stretchy(word):
                count += 1
        
        return count
