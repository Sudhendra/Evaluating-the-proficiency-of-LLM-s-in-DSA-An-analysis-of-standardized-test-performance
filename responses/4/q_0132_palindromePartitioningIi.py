class Solution:
    def minCut(self, s: str) -> int:
        n = len(s)
        is_palindrome = [[False] * n for _ in range(n)]
        dp = [0] * n

        for i in range(n):
            min_cuts = i
            for j in range(i, -1, -1):
                if s[i] == s[j] and (i - j < 2 or is_palindrome[j + 1][i - 1]):
                    is_palindrome[j][i] = True
                    min_cuts = 0 if j == 0 else min(min_cuts, 1 + dp[j - 1])

            dp[i] = min_cuts

        return dp[n - 1]
