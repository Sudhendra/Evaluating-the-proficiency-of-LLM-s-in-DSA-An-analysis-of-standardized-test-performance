from typing import List

class Solution:
    def tallestBillboard(self, rods: List[int]) -> int:
        dp = {0: 0}
        
        for rod in rods:
            for diff, height in list(dp.items()):
                dp[diff + rod] = max(dp.get(diff + rod, 0), height)
                dp[abs(diff - rod)] = max(dp.get(abs(diff - rod), 0), height + min(diff, rod))
        
        return dp[0]
