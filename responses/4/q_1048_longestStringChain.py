from collections import defaultdict

class Solution:
    def longestStrChain(self, words: List[str]) -> int:
        words.sort(key=len)
        word_chain_length = defaultdict(int)
        
        for word in words:
            for i in range(len(word)):
                prev_word = word[:i] + word[i+1:]
                word_chain_length[word] = max(word_chain_length[word], word_chain_length.get(prev_word, 0) + 1)
        
        return max(word_chain_length.values())
