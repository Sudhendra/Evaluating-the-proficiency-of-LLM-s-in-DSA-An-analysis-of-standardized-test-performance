from collections import defaultdict

class Solution:
    def longestStrChain(self, words: List[str]) -> int:
        dp = defaultdict(int)
        words.sort(key=len)  # Sorting words by length to optimize DP

        for word in words:
            for i in range(len(word)):
                prev_word = word[:i] + word[i+1:]
                dp[word] = max(dp[word], dp.get(prev_word, 0) + 1)

        return max(dp.values())
