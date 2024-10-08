class Solution:
    def findRotateSteps(self, ring: str, key: str) -> int:
        from collections import defaultdict
        
        def distance(p1, p2, n):
            return min(abs(p1 - p2), n - abs(p1 - p2))
        
        n, m = len(ring), len(key)
        positions = defaultdict(list)
        
        for i, c in enumerate(ring):
            positions[c].append(i)
        
        dp = [[float('inf')] * m for _ in range(n)]
        
        for pos in positions[key[0]]:
            dp[pos][0] = min(pos, n - pos) + 1
        
        for i in range(1, m):
            for cur in positions[key[i]]:
                for prev in positions[key[i-1]]:
                    dp[cur][i] = min(dp[cur][i], dp[prev][i-1] + distance(prev, cur, n) + 1)
        
        return min(dp[i][m-1] for i in range(n))

# If you have multiple solutions, add them all here as methods of the same class.
