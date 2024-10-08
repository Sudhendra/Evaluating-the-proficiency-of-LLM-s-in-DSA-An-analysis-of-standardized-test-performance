from itertools import permutations

class Solution:
    def tallestBillboard(self, rods: List[int]) -> int:
        dp = {0: 0}
        
        for rod in rods:
            for s, h in list(dp.items()):
                dp[s + rod] = max(dp.get(s + rod, 0), h)
                dp[abs(s - rod)] = max(dp.get(abs(s - rod), 0), h + min(s, rod))
        
        return dp[0]