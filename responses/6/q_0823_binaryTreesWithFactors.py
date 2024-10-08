from collections import Counter

class Solution:
    def numFactoredBinaryTrees(self, arr: List[int]) -> int:
        arr.sort()
        dp = Counter()
        mod = 10**9 + 7

        for num in arr:
            dp[num] = 1
            for smaller_num in arr:
                if smaller_num * smaller_num > num:
                    break
                if num % smaller_num == 0 and num // smaller_num in dp:
                    dp[num] += dp[smaller_num] * dp[num // smaller_num] % mod

        return sum(dp.values()) % mod
