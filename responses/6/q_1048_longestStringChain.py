from collections import defaultdict

class Solution:
    def longestStrChain(self, words: List[str]) -> int:
        words.sort(key=len)  # Sort words by length

        dp = defaultdict(int)  # Dictionary to store the longest chain ending at each word
        max_chain_length = 1

        for word in words:
            for i in range(len(word)):
                prev_word = word[:i] + word[i+1:]  # Remove one character at index i
                dp[word] = max(dp[word], dp.get(prev_word, 0) + 1)
                max_chain_length = max(max_chain_length, dp[word])

        return max_chain_length
