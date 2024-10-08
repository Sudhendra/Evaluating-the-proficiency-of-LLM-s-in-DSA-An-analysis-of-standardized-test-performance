from typing import List

class Solution:
    def minimumTotal(self, triangle: List[List[int]]) -> int:
        if not triangle:
            return 0
        
        dp = [0] * len(triangle[-1])
        dp[0] = triangle[0][0]
        
        for i in range(1, len(triangle)):
            temp_dp = dp.copy()  # Make a copy of current dp array
            for j in range(len(triangle[i])):
                if j == 0:
                    dp[j] = temp_dp[j] + triangle[i][j]
                elif j == len(triangle[i]) - 1:
                    dp[j] = temp_dp[j-1] + triangle[i][j]
                else:
                    dp[j] = min(temp_dp[j-1], temp_dp[j]) + triangle[i][j]
        
        return min(dp)
