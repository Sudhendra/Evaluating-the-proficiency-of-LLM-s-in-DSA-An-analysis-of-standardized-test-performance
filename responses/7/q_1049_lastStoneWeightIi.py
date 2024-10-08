from typing import List

class Solution:
    def lastStoneWeightII(self, stones: List[int]) -> int:
        total_sum = sum(stones)
        target = total_sum // 2
        dp = [0] * (target + 1)

        for stone in stones:
            for j in range(target, stone-1, -1):
                dp[j] = max(dp[j], dp[j - stone] + stone)

        return total_sum - 2 * dp[target]
