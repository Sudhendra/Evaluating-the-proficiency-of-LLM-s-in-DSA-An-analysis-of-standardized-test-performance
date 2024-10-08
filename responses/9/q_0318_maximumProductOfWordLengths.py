from typing import List

class Solution:
    
    def maxProduct(self, words: List[str]) -> int:
        def has_common_letters(word1, word2):
            return any(letter in word2 for letter in word1)
        
        max_product = 0
        word_length = {}
        
        for word in words:
            bitmask = 0
            for char in word:
                bitmask |= 1 << (ord(char) - ord('a'))
            word_length[bitmask] = max(word_length.get(bitmask, 0), len(word))
        
        for bitmask1, len1 in word_length.items():
            for bitmask2, len2 in word_length.items():
                if not bitmask1 & bitmask2:
                    max_product = max(max_product, len1 * len2)
        
        return max_product
