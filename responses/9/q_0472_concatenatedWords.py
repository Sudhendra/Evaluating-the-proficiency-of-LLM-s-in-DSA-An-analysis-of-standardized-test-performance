from typing import List

class Solution:
    def findAllConcatenatedWordsInADict(self, words: List[str]) -> List[str]:
        word_set = set(words)
        memo = {}

        def dfs(word):
            if word in memo:
                return memo[word]
            for i in range(1, len(word)):
                prefix, suffix = word[:i], word[i:]
                if prefix in word_set and (suffix in word_set or dfs(suffix)):
                    memo[word] = True
                    return True
            memo[word] = False
            return False
        
        res = []
        for word in words:
            word_set.remove(word)
            if dfs(word):
                res.append(word)
            word_set.add(word)

        return res
