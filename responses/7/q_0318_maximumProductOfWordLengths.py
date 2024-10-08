from typing import List

class Solution:
    def maxProduct(self, words: List[str]) -> int:
        max_product = 0
        word_bits = [0] * len(words)
        
        for i, word in enumerate(words):
            for char in word:
                word_bits[i] |= 1 << (ord(char) - ord('a'))
        
        for i in range(len(words)):
            for j in range(i+1, len(words)):
                if word_bits[i] & word_bits[j] == 0:
                    max_product = max(max_product, len(words[i]) * len(words[j]))
        
        return max_product
