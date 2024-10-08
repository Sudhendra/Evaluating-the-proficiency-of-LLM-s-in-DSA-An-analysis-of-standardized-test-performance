class Solution:
    def minFlipsMonoIncr(self, s: str) -> int:
        n = len(s)
        dp = [0] * (n + 1)
        for i in range(1, n + 1):
            dp[i] = dp[i-1] + int(s[i-1] == '1')
        
        result = dp[n]
        flips = dp[n]
        
        for i in range(0, n):
            flips = min(flips, i - dp[i] + dp[n] - dp[i])
        
        result = min(result, flips)
        
        return result
