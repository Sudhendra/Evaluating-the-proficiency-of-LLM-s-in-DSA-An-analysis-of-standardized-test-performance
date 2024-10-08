from collections import defaultdict

class Solution:
    def numFactoredBinaryTrees(self, arr: List[int]) -> int:
        MOD = 10**9 + 7
        arr.sort()
        dp = defaultdict(int)
        
        for num in arr:
            dp[num] = 1
            for x in arr:
                if x <= num // 2:
                    y = num // x
                    if y in dp:
                        dp[num] += dp[x] * dp[y]
                        dp[num] %= MOD
                        
        return sum(dp.values()) % MOD
