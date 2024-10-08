from typing import List

class Solution:
    def lastStoneWeightII(self, stones: List[int]) -> int:
        total_sum = sum(stones)
        max_weight = total_sum // 2  # Calculate the maximum possible weight that can be obtained

        dp = [0] * (max_weight + 1)
        for stone in stones:
            for j in range(max_weight, stone - 1, -1):
                dp[j] = max(dp[j], dp[j - stone] + stone)

        return total_sum - 2 * dp[max_weight]
