class Solution:
    def minFlipsMonoIncr(self, s: str) -> int:
        dp = [0, 0]
        for i in s:
            dp[int(i)] = dp[int(i)] + 1 if int(i) == 1 else dp[int(i)]
            dp[1] = min(dp)
        return dp[1]