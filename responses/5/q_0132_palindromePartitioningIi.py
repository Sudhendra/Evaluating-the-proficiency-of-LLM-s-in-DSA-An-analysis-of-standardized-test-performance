class Solution:
    def minCut(self, s: str) -> int:
        n = len(s)
        dp = [0] * n
        is_palindrome = [[False] * n for _ in range(n)]

        for end in range(n):
            min_cuts = end
            for start in range(end + 1):
                if s[start] == s[end] and (end - start <= 2 or is_palindrome[start + 1][end - 1]):
                    is_palindrome[start][end] = True
                    if start == 0:
                        min_cuts = 0
                    else:
                        min_cuts = min(min_cuts, dp[start - 1] + 1)
            dp[end] = min_cuts

        return dp[n - 1]
