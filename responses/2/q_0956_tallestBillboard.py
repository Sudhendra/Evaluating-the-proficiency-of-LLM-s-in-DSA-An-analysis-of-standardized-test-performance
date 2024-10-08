from typing import List

class Solution:
    def tallestBillboard(self, rods: List[int]) -> int:
        dp = {0: 0}
        for rod in rods:
            new_dp = dp.copy()
            for diff, height in dp.items():
                new_dp[diff + rod] = max(new_dp.get(diff + rod, 0), height)
                new_dp[abs(diff - rod)] = max(new_dp.get(abs(diff - rod), 0), height + min(diff, rod))
            dp = new_dp
        return dp[0]