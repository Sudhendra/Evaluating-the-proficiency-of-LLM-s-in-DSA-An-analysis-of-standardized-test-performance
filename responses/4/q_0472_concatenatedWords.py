from typing import List

class Solution:
    def findAllConcatenatedWordsInADict(self, words: List[str]) -> List[str]:
        def can_form(word, word_set):
            if not word_set:
                return False
            n = len(word)
            dp = [False] * (n + 1)
            dp[0] = True
            for i in range(1, n + 1):
                for j in range(i):
                    if not dp[j]:
                        continue
                    if word[j:i] in word_set:
                        dp[i] = True
                        break
            return dp[n]

        words.sort(key=lambda x: len(x))
        res = []
        word_set = set()
        for word in words:
            if can_form(word, word_set):
                res.append(word)
            word_set.add(word)
        return res
