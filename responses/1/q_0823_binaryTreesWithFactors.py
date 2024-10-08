class Solution:
    def numFactoredBinaryTrees(self, arr: List[int]) -> int:
        MOD = 10**9 + 7
        arr.sort()
        dp = {}
        
        for i, num in enumerate(arr):
            dp[num] = 1
            for j in range(i):
                if num % arr[j] == 0 and num//arr[j] in dp:
                    dp[num] += dp[arr[j]] * dp[num//arr[j]]
                    dp[num] %= MOD
        
        return sum(dp.values()) % MOD