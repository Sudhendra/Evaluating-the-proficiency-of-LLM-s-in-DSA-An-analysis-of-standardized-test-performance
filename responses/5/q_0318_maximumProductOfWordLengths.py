from typing import List

class Solution:
    def maxProduct(self, words: List[str]) -> int:
        n = len(words)
        mask = [0] * n
        bit_len = [0] * n
        max_product = 0

        for i, word in enumerate(words):
            for char in word:
                mask[i] |= 1 << (ord(char) - 97)
            bit_len[i] = len(word)

        for i in range(n):
            for j in range(i+1, n):
                if mask[i] & mask[j] == 0:
                    product = bit_len[i] * bit_len[j]
                    max_product = max(max_product, product)

        return max_product
