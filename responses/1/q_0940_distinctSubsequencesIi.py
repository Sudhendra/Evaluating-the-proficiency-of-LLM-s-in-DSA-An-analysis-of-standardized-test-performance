class Solution:
    def distinctSubseqII(self, s: str) -> int:
        dp = [0] * 26
        mod = 10**9 + 7

        for char in s:
            dp[ord(char) - ord('a')] = sum(dp) + 1
        return sum(dp) % mod
