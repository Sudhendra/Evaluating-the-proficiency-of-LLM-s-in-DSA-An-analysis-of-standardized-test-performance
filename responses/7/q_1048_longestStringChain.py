from collections import defaultdict

class Solution:
    def longestStrChain(self, words: List[str]) -> int:
        words.sort(key=len)  # sort the words by length

        dp = defaultdict(int)  # dictionary to store the length of the longest chain ending at each word

        for word in words:
            for i in range(len(word)):
                pred = word[:i] + word[i+1:]  # generate all possible predecessors by removing one character

                dp[word] = max(dp[word], dp.get(pred, 0) + 1)  # update the longest chain length for current word

        return max(dp.values())  # return the maximum chain length

    # If you have multiple solutions, add them all here as methods of the same class.
