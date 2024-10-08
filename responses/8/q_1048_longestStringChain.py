from collections import defaultdict

class Solution:
    def longestStrChain(self, words: List[str]) -> int:
        words.sort(key=len)
        word_chain_length = defaultdict(int)
        max_length = 1

        for word in words:
            for i in range(len(word)):
                predecessor = word[:i] + word[i+1:]
                word_chain_length[word] = max(word_chain_length[word], word_chain_length.get(predecessor, 0) + 1)
                max_length = max(max_length, word_chain_length[word])

        return max_length
