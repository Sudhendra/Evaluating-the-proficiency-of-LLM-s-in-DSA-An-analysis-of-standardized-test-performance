from collections import defaultdict

class Solution:
    def tallestBillboard(self, rods: List[int]) -> int:
        dp = defaultdict(int)
        dp[0] = 0

        for rod in rods:
            new_dp = dp.copy()
            for diff in dp:
                new_dp[diff + rod] = max(dp[diff + rod], dp[diff])
                new_dp[abs(diff - rod)] = max(dp[abs(diff - rod)], dp[diff] + min(rod, diff))
            dp = new_dp

        return dp[0]
