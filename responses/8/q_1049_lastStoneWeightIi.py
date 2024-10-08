class Solution:
    def lastStoneWeightII(self, stones: List[int]) -> int:
        total_sum = sum(stones)
        max_weight = total_sum // 2
        dp = [0] * (max_weight + 1)
        
        for stone in stones:
            for weight in range(max_weight, stone - 1, -1):
                dp[weight] = max(dp[weight], dp[weight - stone] + stone)
        
        return total_sum - 2 * dp[max_weight]
