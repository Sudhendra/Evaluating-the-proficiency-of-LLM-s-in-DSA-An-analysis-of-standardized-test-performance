from typing import List

class Solution:
    def findAllConcatenatedWordsInADict(self, words: List[str]) -> List[str]:
        word_set = set(words)

        def dfs(word):
            for i in range(1, len(word)):
                prefix, suffix = word[:i], word[i:]
                if prefix in word_set and (suffix in word_set or dfs(suffix)):
                    return True
            return False

        result = []
        for word in words:
            word_set.remove(word)
            if dfs(word):
                result.append(word)
            word_set.add(word)

        return result
