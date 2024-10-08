from collections import defaultdict
class Solution:
    def numFactoredBinaryTrees(self, arr: List[int]) -> int:
        MOD = 10**9 + 7
        arr.sort()
        dp = defaultdict(int)
        for num in arr:
            dp[num] = 1
            for factor1 in arr:
                factor2 = num / factor1
                if factor2 in dp:
                    dp[num] += dp[factor1] * dp[factor2]
                    dp[num] %= MOD
        return sum(dp.values()) % MOD
