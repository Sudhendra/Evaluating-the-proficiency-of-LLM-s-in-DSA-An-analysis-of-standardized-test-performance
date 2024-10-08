from typing import List

class Solution:
    def findAllConcatenatedWordsInADict(self, words: List[str]) -> List[str]:
        word_set = set(words)
        concatenated_words = []

        def dfs(word):
            for i in range(1, len(word)):
                prefix, suffix = word[:i], word[i:]
                if prefix in word_set and suffix in word_set:
                    return True
                if prefix in word_set and dfs(suffix):
                    return True
            return False

        for word in words:
            word_set.remove(word)
            if dfs(word):
                concatenated_words.append(word)
            word_set.add(word)

        return concatenated_words
