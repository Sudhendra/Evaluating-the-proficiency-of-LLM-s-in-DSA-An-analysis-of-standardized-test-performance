from typing import List

class Solution:
    def isAlienSorted(self, words: List[str], order: str) -> bool:
        alien_dict = {c: i for i, c in enumerate(order)}
        
        for i in range(len(words) - 1):
            word1, word2 = words[i], words[i + 1]
            for j in range(min(len(word1), len(word2))):
                if word1[j] != word2[j]:
                    if alien_dict[word1[j]] > alien_dict[word2[j]]:
                        return False
                    break
            else:
                if len(word1) > len(word2):
                    return False
        
        return True
