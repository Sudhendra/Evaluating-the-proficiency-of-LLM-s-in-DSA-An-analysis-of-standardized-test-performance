from typing import List

class Solution:
    def mergeStones(self, stones: List[int], k: int) -> int:
        n = len(stones)
        if (n - 1) % (k - 1) != 0:
            return -1

        prefix_sum = [0] * (n + 1)
        for i in range(n):
            prefix_sum[i + 1] = prefix_sum[i] + stones[i]

        dp = [[0] * n for _ in range(n)]
        for length in range(k, n + 1):
            for i in range(n - length + 1):
                j = i + length - 1
                dp[i][j] = float('inf')
                for mid in range(i, j, k - 1):
                    dp[i][j] = min(dp[i][j], dp[i][mid] + dp[mid + 1][j])
                if (j - i) % (k - 1) == 0:
                    dp[i][j] += prefix_sum[j + 1] - prefix_sum[i]

        return dp[0][n - 1]

# Example usage
solution = Solution()
print(solution.mergeStones([3, 2, 4, 1], 2))  # Output: 20
print(solution.mergeStones([3, 2, 4, 1], 3))  # Output: -1
print(solution.mergeStones([3, 5, 1, 2, 6], 3))  # Output: 25
