class Solution:
    def soupServings(self, n: int) -> float:
        if n >= 4800:
            return 1.0
        memo = {}
        
        def dp(soup_A, soup_B):
            if (soup_A, soup_B) in memo:
                return memo[(soup_A, soup_B)]
            
            if soup_A <= 0 and soup_B <= 0:
                return 0.5
            if soup_A <= 0:
                return 1.0
            if soup_B <= 0:
                return 0.0

            memo[(soup_A, soup_B)] = 0.25 * (
                    dp(soup_A - 100, soup_B) +
                    dp(soup_A - 75, soup_B - 25) +
                    dp(soup_A - 50, soup_B - 50) +
                    dp(soup_A - 25, soup_B - 75)
            )
            return memo[(soup_A, soup_B)]

        return dp(n, n)