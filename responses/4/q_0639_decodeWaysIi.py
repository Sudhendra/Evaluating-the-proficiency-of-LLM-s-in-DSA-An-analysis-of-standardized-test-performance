class Solution:
    def numDecodings(self, s: str) -> int:
        MOD = 10**9 + 7
        dp = [1, 0, 0]  # Number of ways to decode s[i-2], s[i-1], s[i]
        
        for c in s:
            dp_new = [0, 0, 0]
            if c == '*':
                dp_new[0] = 9 * dp[0] + 9 * dp[1] + 6 * dp[2]  # Single digit mapping
                dp_new[1] = dp[0]  # Two digits starting with 1
                dp_new[2] = dp[0]  # Two digits starting with 2
            else:
                dp_new[0] = (c > '0') * dp[0] + dp[1] + (c <= '6') * dp[2]  # Single digit mapping
                dp_new[1] = (c == '1') * dp[0]  # Two digits starting with 1
                dp_new[2] = (c == '2') * dp[0]  # Two digits starting with 2

            dp = [x % MOD for x in dp_new]
        
        return dp[0]
