class Solution:
    def minFlipsMonoIncr(self, s: str) -> int:
        n = len(s)
        dp = [0] * (n + 1)
        
        for i in range(1, n+1):
            dp[i] = dp[i-1] + int(s[i-1] == '1')
        
        ans = dp[n]
        zeros = dp[n]
        
        for i in range(n):
            zeros = min(zeros, dp[i] + (n - i - (dp[n] - dp[i])))
            ans = min(ans, dp[i] + zeros)
        
        return ans
