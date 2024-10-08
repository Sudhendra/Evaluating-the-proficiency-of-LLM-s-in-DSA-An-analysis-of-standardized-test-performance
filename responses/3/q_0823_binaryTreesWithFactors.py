from collections import defaultdict

class Solution:
    def numFactoredBinaryTrees(self, arr: List[int]) -> int:
        arr.sort()
        dp = defaultdict(int)
        for i, num in enumerate(arr):
            dp[num] = 1
            for j in range(i):
                if num % arr[j] == 0 and num // arr[j] in dp:
                    dp[num] += dp[arr[j]] * dp[num // arr[j]]
        return sum(dp.values()) % (10**9 + 7)
