from typing import List

class Solution:
    def minDeletionSize(self, strs: List[str]) -> int:
        n = len(strs)
        m = len(strs[0])
        
        dp = [1] * m
        
        for j in range(1, m):
            for i in range(j):
                if all(strs[k][i] <= strs[k][j] for k in range(n)):
                    dp[j] = max(dp[j], dp[i] + 1)
        
        return m - max(dp)
