from collections import defaultdict

class Solution:
    def longestStrChain(self, words: List[str]) -> int:
        words.sort(key=len)
        word_chain = defaultdict(int)
        result = 1

        for word in words:
            curr_len = 1
            for i in range(len(word)):
                predecessor = word[:i] + word[i+1:]
                curr_len = max(curr_len, word_chain[predecessor] + 1)
            word_chain[word] = curr_len
            result = max(result, curr_len)

        return result
