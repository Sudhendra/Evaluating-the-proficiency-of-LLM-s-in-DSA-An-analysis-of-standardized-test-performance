from typing import List

class Solution:
    
    def maxProduct(self, words: List[str]) -> int:
        def has_common_letter(word1, word2):
            return any(letter in word2 for letter in word1)
        
        max_product = 0
        word_bits = [0] * len(words)
        
        for i, word in enumerate(words):
            for letter in word:
                word_bits[i] |= 1 << (ord(letter) - ord('a'))
        
        for i in range(len(words)):
            for j in range(i+1, len(words)):
                if not has_common_letter(words[i], words[j]):
                    max_product = max(max_product, len(words[i]) * len(words[j]))
        
        return max_product
