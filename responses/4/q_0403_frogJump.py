from collections import defaultdict

class Solution:
    def canCross(self, stones: List[int]) -> bool:
        if stones[1] != 1:
            return False
        
        n = len(stones)
        if n == 2:
            return True
        
        dp = defaultdict(set)
        dp[1] = set([1])
        
        for i in range(2, n):
            for j in range(1, i):
                diff = stones[i] - stones[j]
                if diff in dp[j]:
                    dp[i].add(diff)
                    dp[i].add(diff + 1)
                    if diff - 1 > 0:
                        dp[i].add(diff - 1)
                    
        return len(dp[n-1]) > 0
