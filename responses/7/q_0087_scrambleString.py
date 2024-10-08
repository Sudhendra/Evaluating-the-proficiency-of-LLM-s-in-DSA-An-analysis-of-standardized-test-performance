class Solution:
    def isScramble(self, s1: str, s2: str) -> bool:
        if s1 == s2:
            return True
        if len(s1) != len(s2) or sorted(s1) != sorted(s2):
            return False
        
        n = len(s1)
        dp = [[[False] * n for _ in range(n)] for _ in range(n)]

        for i in range(n):
            for j in range(n):
                dp[0][i][j] = s1[i] == s2[j]

        for k in range(2, n + 1):
            for i in range(n - k, -1, -1):
                for j in range(n - k, -1, -1):
                    for l in range(1, k):
                        if (dp[l - 1][i][j] and dp[k - l - 1][i + l][j + l]) or (dp[l - 1][i][j + k - l] and dp[k - l - 1][i + l][j]):
                            dp[k - 1][i][j] = True
                            break

        return dp[n - 1][0][0]
