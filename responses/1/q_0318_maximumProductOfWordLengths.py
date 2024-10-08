from typing import List

class Solution:
    def maxProduct(self, words: List[str]) -> int:
        def word_to_bitmask(word):
            bitmask = 0
            for char in word:
                bitmask |= 1 << (ord(char) - ord('a'))
            return bitmask

        N = len(words)
        bitmask_list = [word_to_bitmask(word) for word in words]

        max_product = 0
        for i in range(N):
            for j in range(i+1, N):
                if bitmask_list[i] & bitmask_list[j] == 0:
                    max_product = max(max_product, len(words[i]) * len(words[j]))

        return max_product