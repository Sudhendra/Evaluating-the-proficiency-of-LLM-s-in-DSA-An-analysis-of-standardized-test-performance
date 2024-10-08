class Solution:
    def soupServings(self, n: int) -> float:
        if n >= 5000:
            return 1.0
        memo = {}
        
        def serve(a, b):
            if (a, b) in memo:
                return memo[(a, b)]
            
            if a <= 0 and b <= 0:  # Both are empty at the same time
                return 0.5
            if a <= 0:  # A becomes empty first
                return 1.0
            if b <= 0:  # B becomes empty first
                return 0.0
            
            memo[(a, b)] = 0.25 * (
                serve(a-100, b) + 
                serve(a-75, b-25) + 
                serve(a-50, b-50) + 
                serve(a-25, b-75)
            )
            return memo[(a, b)]
        
        return serve(n, n)
