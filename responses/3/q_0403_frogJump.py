class Solution:
    def canCross(self, stones: List[int]) -> bool:
        if stones[1] != 1:
            return False
        
        n = len(stones)
        dp = [set() for _ in range(n)]
        dp[1].add(1)
        
        for i in range(2, n):
            for j in range(1, i):
                dist = stones[i] - stones[j]
                if dist in dp[j]:
                    dp[i].add(dist)
                    dp[i].add(dist - 1)
                    dp[i].add(dist + 1)
        
        return len(dp[-1]) > 0