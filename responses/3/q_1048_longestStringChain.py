from collections import defaultdict

class Solution:
    def longestStrChain(self, words: List[str]) -> int:
        words.sort(key=len)
        word_to_len = defaultdict(int)
        max_chain_length = 1
        
        for word in words:
            if word not in word_to_len:
                word_to_len[word] = 1
                
            for i in range(len(word)):
                predecessor = word[:i] + word[i+1:]
                if predecessor in word_to_len:
                    word_to_len[word] = max(word_to_len[word], word_to_len[predecessor] + 1)
                
            max_chain_length = max(max_chain_length, word_to_len[word])
        
        return max_chain_length
