class Solution:

    def distinctSubseqII(self, s: str) -> int:
        MOD = 10**9 + 7
        dp = [0] * 26
        for char in s:
            dp[ord(char) - ord('a')] = sum(dp) + 1 % MOD
        return sum(dp) % MOD