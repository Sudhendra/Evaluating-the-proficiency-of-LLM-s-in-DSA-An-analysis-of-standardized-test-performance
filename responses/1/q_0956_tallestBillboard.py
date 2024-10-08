from typing import List

class Solution:
    def tallestBillboard(self, rods: List[int]) -> int:
        dp = {0: 0}
        for rod in rods:
            for key, val in list(dp.items()):
                dp[key + rod] = max(dp.get(key + rod, 0), val)
                dp[abs(key - rod)] = max(dp.get(abs(key - rod), 0), val + min(key, rod))
        return dp[0]