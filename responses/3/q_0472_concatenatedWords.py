class Solution:
    def findAllConcatenatedWordsInADict(self, words: List[str]) -> List[str]:
        def dfs(word, word_set):
            if word in word_set:
                return True
            for i in range(1, len(word)):
                prefix = word[:i]
                if prefix in word_set:
                    if dfs(word[i:], word_set):
                        return True
            return False

        words_set = set(words)
        result = []
        for word in words:
            words_set.remove(word)
            if dfs(word, words_set):
                result.append(word)
            words_set.add(word)

        return result
