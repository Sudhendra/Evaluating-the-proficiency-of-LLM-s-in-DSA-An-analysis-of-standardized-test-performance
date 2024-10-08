from collections import defaultdict

class Solution:
    def longestStrChain(self, words: List[str]) -> int:
        words.sort(key=len)
        dp = defaultdict(int)
        for word in words:
            for i in range(len(word)):
                predecessor = word[:i] + word[i+1:]
                dp[word] = max(dp[word], dp.get(predecessor, 0) + 1)
        return max(dp.values()) or 1
