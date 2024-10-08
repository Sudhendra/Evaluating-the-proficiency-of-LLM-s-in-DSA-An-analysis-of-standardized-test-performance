class Solution:
    def minCut(self, s: str) -> int:
        n = len(s)
        dp = [0] * n
        palindromes = [[False] * n for _ in range(n)]

        for i in range(n):
            min_cuts = i
            for j in range(i + 1):
                if s[i] == s[j] and (i - j < 2 or palindromes[j + 1][i - 1]):
                    palindromes[j][i] = True
                    if j == 0:
                        min_cuts = 0
                    else:
                        min_cuts = min(min_cuts, dp[j - 1] + 1)
            dp[i] = min_cuts

        return dp[n - 1]