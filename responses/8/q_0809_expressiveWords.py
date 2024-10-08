from typing import List

class Solution:
    
    def expressiveWords(self, s: str, words: List[str]) -> int:
        def is_stretchy(word, s):
            i, j, n, m = 0, 0, len(word), len(s)
            for i in range(m):
                if j < n and word[j] == s[i]:
                    j += 1
                elif s[i - 1:i + 2] != s[i] * 3 != s[i - 2:i + 1]:
                    return False
            return j == n

        count = 0
        for word in words:
            if is_stretchy(word, s):
                count += 1
        return count
