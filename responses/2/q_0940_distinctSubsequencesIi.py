class Solution:
    
    def distinctSubseqII(self, s: str) -> int:
        MOD = 10**9 + 7
        dp = [0] * 26
        total = 1
        for ch in s:
            old_total = total
            total = total * 2 - dp[ord(ch) - ord('a')]
            dp[ord(ch) - ord('a')] = old_total
            total %= MOD
        return (total - 1) % MOD