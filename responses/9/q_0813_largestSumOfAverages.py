from typing import List

class Solution:
    def largestSumOfAverages(self, nums: List[int], k: int) -> float:
        n = len(nums)
        prefix_sum = [0] * (n + 1)

        for i in range(1, n + 1):
            prefix_sum[i] = prefix_sum[i - 1] + nums[i - 1]

        dp = [0.0] * n

        for i in range(n):
            dp[i] = (prefix_sum[n] - prefix_sum[i]) / (n - i)

        for _ in range(k - 1):
            for i in range(n):
                for j in range(i + 1, n):
                    dp[i] = max(dp[i], dp[j] + (prefix_sum[j] - prefix_sum[i]) / (j - i))

        return dp[0]

# Example usage:
solution = Solution()
nums1, k1 = [9, 1, 2, 3, 9], 3
print(solution.largestSumOfAverages(nums1, k1))  # Output: 20.0

nums2, k2 = [1, 2, 3, 4, 5, 6, 7], 4
print(solution.largestSumOfAverages(nums2, k2))  # Output: 20.5
