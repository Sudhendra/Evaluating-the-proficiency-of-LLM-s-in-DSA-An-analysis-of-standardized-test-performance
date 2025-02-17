from collections import defaultdict

class Solution:
    def longestStrChain(self, words: List[str]) -> int:
        words.sort(key=len)
        word_chain_len = defaultdict(int)
        max_length = 1
        
        for word in words:
            for i in range(len(word)):
                prev_word = word[:i] + word[i+1:]
                word_chain_len[word] = max(word_chain_len[word], word_chain_len.get(prev_word, 0) + 1)
            max_length = max(max_length, word_chain_len[word])
        
        return max_length
