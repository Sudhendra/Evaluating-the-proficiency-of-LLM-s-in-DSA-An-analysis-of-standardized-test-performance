from typing import List

class Solution:
    def isAlienSorted(self, words: List[str], order: str) -> bool:
        dict_order = {char: idx for idx, char in enumerate(order)}

        def compare(word1, word2):
            i = 0
            while i < len(word1) and i < len(word2):
                if dict_order[word1[i]] < dict_order[word2[i]]:
                    return True
                elif dict_order[word1[i]] > dict_order[word2[i]]:
                    return False
                i += 1
            return len(word1) <= len(word2)

        for i in range(len(words) - 1):
            if not compare(words[i], words[i + 1]):
                return False
        return True
