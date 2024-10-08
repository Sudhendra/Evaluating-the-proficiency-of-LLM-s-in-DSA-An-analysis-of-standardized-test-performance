class Solution:
    def distinctSubseqII(self, s: str) -> int:
        mod = 10**9 + 7
        dp = [0] * (len(s) + 1)
        last_occurrence = [-1] * 26
        dp[0] = 1

        for i in range(1, len(s) + 1):
            dp[i] = (2 * dp[i - 1]) % mod
            if last_occurrence[ord(s[i - 1]) - ord('a')] != -1:
                dp[i] = (dp[i] - dp[last_occurrence[ord(s[i - 1]) - ord('a')]]) % mod
            last_occurrence[ord(s[i - 1]) - ord('a')] = i - 1

        return (dp[-1] - 1) % mod
