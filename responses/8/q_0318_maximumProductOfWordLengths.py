from typing import List

class Solution:
    def maxProduct(self, words: List[str]) -> int:
        max_len = 0
        word_set = [set(word) for word in words]
        
        for i in range(len(words) - 1):
            for j in range(i + 1, len(words)):
                if not word_set[i] & word_set[j]:
                    max_len = max(max_len, len(words[i]) * len(words[j]))
        
        return max_len
