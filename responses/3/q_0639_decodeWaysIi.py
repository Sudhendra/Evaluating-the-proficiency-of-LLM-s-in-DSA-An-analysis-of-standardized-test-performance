class Solution:
    def numDecodings(self, s: str) -> int:
        mod = 10**9 + 7
        if not s or s[0] == '0':
            return 0

        dp = [0] * (len(s) + 1)
        dp[0], dp[1] = 1, 9 if s[0] == '*' else 1

        for i in range(2, len(s) + 1):
            if s[i - 1] == '0':
                if s[i - 2] == '1' or s[i - 2] == '2':
                    dp[i] += dp[i - 2]
                elif s[i - 2] == '*':
                    dp[i] += 2 * dp[i - 2]
                else:
                    return 0
            elif s[i - 1] == '*':
                dp[i] += 9 * dp[i - 1]
                if s[i - 2] == '1':
                    dp[i] += 9 * dp[i - 2]
                elif s[i - 2] == '2':
                    dp[i] += 6 * dp[i - 2]
                elif s[i - 2] == '*':
                    dp[i] += 15 * dp[i - 2]
            else:
                dp[i] += dp[i - 1]
                if s[i - 2] == '1' or (s[i - 2] == '2' and s[i - 1] <= '6'):
                    dp[i] += dp[i - 2]
                elif s[i - 2] == '*':
                    dp[i] += (2 if s[i - 1] <= '6' else 1) * dp[i - 2]
            dp[i] %= mod

        return dp[-1]
