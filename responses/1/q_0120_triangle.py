class Solution:
    def minimumTotal(self, triangle: List[List[int]]) -> int:
        n = len(triangle)
        dp = triangle[-1] # Initialize dp with values from the last row of the triangle
        
        for layer in range(n-2, -1, -1):
            for i in range(len(triangle[layer])):
                dp[i] = triangle[layer][i] + min(dp[i], dp[i+1])
        
        return dp[0]