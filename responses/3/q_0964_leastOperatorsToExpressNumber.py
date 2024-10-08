class Solution:
    def leastOpsExpressTarget(self, x: int, target: int) -> int:
        pos = [0] * 22
        neg = [0] * 22

        k = 0
        while target:
            pos[k] = target % x
            neg[k] = x - pos[k]
            target //= x
            k += 1

        dp = [0] * 22

        dp[0] = 2 * pos[0]
        for i in range(1, k):
            dp[i] = min(pos[i] * i + dp[i - 1], (pos[i] + 1) * i + dp[i - 1], (neg[i] + 1) * i + dp[i - 1])

        return dp[k - 1] - 1
