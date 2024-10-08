from collections import defaultdict

class Solution:
    def numFactoredBinaryTrees(self, arr: List[int]) -> int:
        mod = 10**9 + 7
        arr.sort()
        dp = defaultdict(int)
        for i, x in enumerate(arr):
            dp[x] = 1
            for j in range(i):
                if x % arr[j] == 0 and x // arr[j] in dp:
                    dp[x] += dp[arr[j]] * dp[x // arr[j]]
                    dp[x] %= mod
        return sum(dp.values()) % mod
