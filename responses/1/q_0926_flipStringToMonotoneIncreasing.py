class Solution:
    def minFlipsMonoIncr(self, s: str) -> int:
        n = len(s)
        dp = [0] * n
        flip_count = s.count('1')
        res = flip_count
        for i in range(n):
            if s[i] == '0':
                res = min(res, flip_count + dp[i])
            else:
                flip_count -= 1
                dp[i] = dp[i - 1] + 1
                res = min(res, flip_count + dp[i])
        return res