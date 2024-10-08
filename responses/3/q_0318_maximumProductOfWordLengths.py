from typing import List

class Solution:
    def maxProduct(self, words: List[str]) -> int:
        bit_values = {}
        for word in words:
            bit_mask = 0
            for char in word:
                bit_mask |= (1 << (ord(char) - ord('a')))
            bit_values[word] = bit_mask
        
        max_product = 0
        for i in range(len(words)):
            for j in range(i+1, len(words)):
                if bit_values[words[i]] & bit_values[words[j]] == 0:
                    max_product = max(max_product, len(words[i]) * len(words[j]))
        
        return max_product
