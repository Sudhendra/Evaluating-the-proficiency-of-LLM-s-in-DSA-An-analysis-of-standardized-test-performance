class Solution:
    
    def findRotateSteps(self, ring: str, key: str) -> int:
        from collections import defaultdict
        positions = defaultdict(list)
        for i, c in enumerate(ring):
            positions[c].append(i)
        
        memo = dict()
        def dp(i, j):
            if i == len(key):
                return 0
            if (i, j) in memo:
                return memo[(i, j)]
            ans = float('inf')
            for pos in positions[key[i]]:
                diff = abs(j - pos)
                diff = min(diff, len(ring) - diff)
                ans = min(ans, diff + 1 + dp(i + 1, pos))
            memo[(i, j)] = ans
            return ans
        
        return dp(0, 0)
