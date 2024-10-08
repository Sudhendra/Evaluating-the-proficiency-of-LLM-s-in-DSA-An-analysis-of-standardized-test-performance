class Solution:
    def lastStoneWeightII(self, stones: List[int]) -> int:
        total_sum = sum(stones)
        n, m = len(stones), total_sum//2
        dp = [0] * (m + 1)
        
        for i in range(n):
            for j in range(m, stones[i] - 1, -1):
                dp[j] = max(dp[j], dp[j - stones[i]] + stones[i])
        
        return total_sum - 2 * dp[m]
