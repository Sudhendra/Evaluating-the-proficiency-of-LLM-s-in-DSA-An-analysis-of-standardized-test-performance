class Solution:
    def soupServings(self, n: int) -> float:
        if n >= 5000:  # As per LeetCode solution
            return 1.0
        
        def dp(a, b, memo):
            if (a, b) in memo:
                return memo[(a, b)]
            if a <= 0 and b <= 0:
                return 0.5
            if a <= 0:
                return 1.0
            if b <= 0:
                return 0.0
            
            memo[(a, b)] = 0.25 * (dp(a-100, b, memo) + dp(a-75, b-25, memo) + dp(a-50, b-50, memo) + dp(a-25, b-75, memo))
            return memo[(a, b)]
        
        return dp(n, n, {})
