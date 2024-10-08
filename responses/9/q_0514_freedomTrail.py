class Solution:
    def findRotateSteps(self, ring: str, key: str) -> int:
        from collections import defaultdict
        lengths = len(ring)
        positions = defaultdict(list)
        for i in range(lengths):
            positions[ring[i]].append(i)
        
        memo = {}
        
        def dp(i, j):  # Returns the minimum steps needed to align ring[i] with key[j]
            if j == len(key):
                return 0
            if (i, j) not in memo:
                memo[(i, j)] = float('inf')
                for k in positions[key[j]]:
                    cost = abs(i - k)
                    cost = min(cost, lengths - cost)
                    memo[(i, j)] = min(memo[(i, j)], cost + 1 + dp(k, j + 1))
            return memo[(i, j)]
        
        return dp(0, 0)
