from typing import List

class Solution:
    def lastStoneWeightII(self, stones: List[int]) -> int:
        total_sum = sum(stones)
        # dp[i] stores whether it is possible to achieve a sum of i using the stones
        dp = [False] * ((total_sum // 2) + 1)
        dp[0] = True
        
        for stone in stones:
            for i in range(total_sum // 2, stone - 1, -1):
                dp[i] = dp[i] or dp[i - stone]
                
        for i in range(total_sum // 2, -1, -1):
            if dp[i]:
                return total_sum - 2 * i
                
        return total_sum   # if no stones are left, return 0