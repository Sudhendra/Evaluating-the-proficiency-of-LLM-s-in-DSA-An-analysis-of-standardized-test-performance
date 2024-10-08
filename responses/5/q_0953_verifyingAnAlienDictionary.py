from typing import List

class Solution:
    def isAlienSorted(self, words: List[str], order: str) -> bool:
        order_map = {char: i for i, char in enumerate(order)}

        def is_sorted(word1, word2):
            i, j = 0, 0
            while i < len(word1) and j < len(word2):
                if order_map[word1[i]] < order_map[word2[j]]:
                    return True
                if order_map[word1[i]] > order_map[word2[j]]:
                    return False
                i += 1
                j += 1

            return len(word1) <= len(word2)

        for i in range(len(words) - 1):
            if not is_sorted(words[i], words[i + 1]):
                return False

        return True
