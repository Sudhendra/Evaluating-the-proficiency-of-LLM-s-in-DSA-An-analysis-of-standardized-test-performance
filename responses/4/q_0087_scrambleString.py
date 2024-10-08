class Solution:
    def isScramble(self, s1: str, s2: str) -> bool:
        if s1 == s2:
            return True
        if sorted(s1) != sorted(s2):
            return False

        n = len(s1)
        dp = [[[False] * n for _ in range(n)] for _ in range(n)]

        for i in range(n):
            for j in range(n):
                dp[0][i][j] = s1[i] == s2[j]

        for l in range(2, n + 1):
            for i in range(n - l + 1):
                for j in range(n - l + 1):
                    for k in range(1, l):
                        if (dp[k - 1][i][j] and dp[l - k - 1][i + k][j + k]) or \
                           (dp[k - 1][i][j + l - k] and dp[l - k - 1][i + k][j]):
                            dp[l - 1][i][j] = True
                            break

        return dp[n - 1][0][0]
