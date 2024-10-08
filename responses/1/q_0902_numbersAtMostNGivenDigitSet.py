class Solution:
    def atMostNGivenDigitSet(self, digits: List[str], n: int) -> int:
        n_str = str(n)
        n_len = len(n_str)
        d_len = len(digits)

        dp = [0] * n_len + [1]

        for i in range(n_len - 1, -1, -1):
            for d in digits:
                if d < n_str[i]:
                    dp[i] += d_len ** (n_len - i - 1)
                elif d == n_str[i]:
                    dp[i] += dp[i + 1]

        for i in range(1, n_len):
            dp[0] += d_len ** i
        
        return dp[0]