from collections import defaultdict

class Solution:
    def numFactoredBinaryTrees(self, arr: List[int]) -> int:
        
        mod = 10**9 + 7
        arr.sort()
        dp = defaultdict(int)
        
        for num in arr:
            dp[num] = 1
            for factor in arr:
                if factor * factor > num:
                    break
                if num % factor == 0:
                    other_factor = num // factor
                    if other_factor in dp:
                        dp[num] += dp[factor] * dp[other_factor] * (1 if factor == other_factor else 2)
                        dp[num] %= mod
        
        return sum(dp.values()) % mod
