class Solution:
    def isAlienSorted(self, words: List[str], order: str) -> bool:
        alien_order = {c: i for i, c in enumerate(order)}
        
        def compare_words(word1, word2):
            n1, n2 = len(word1), len(word2)
            for i in range(min(n1, n2)):
                if alien_order[word1[i]] < alien_order[word2[i]]:
                    return -1
                elif alien_order[word1[i]] > alien_order[word2[i]]:
                    return 1
            return 1 if n1 > n2 else -1
        
        for i in range(1, len(words)):
            if compare_words(words[i-1], words[i]) > 0:
                return False
        
        return True