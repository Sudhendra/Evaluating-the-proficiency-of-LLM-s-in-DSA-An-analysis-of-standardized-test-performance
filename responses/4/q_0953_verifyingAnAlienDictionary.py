from typing import List

class Solution:
    def isAlienSorted(self, words: List[str], order: str) -> bool:
        alien_order = {char: i for i, char in enumerate(order)}
        
        def compare(word1, word2):
            n, m = len(word1), len(word2)
            for i in range(min(n, m)):
                if alien_order[word1[i]] < alien_order[word2[i]]:
                    return -1
                elif alien_order[word1[i]] > alien_order[word2[i]]:
                    return 1
            return -1 if n < m else 0
        
        for i in range(len(words) - 1):
            if compare(words[i], words[i+1]) > 0:
                return False
        return True
