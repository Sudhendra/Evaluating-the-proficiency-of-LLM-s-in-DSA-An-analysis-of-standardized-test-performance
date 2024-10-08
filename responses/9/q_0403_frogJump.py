from collections import defaultdict

class Solution:
    def canCross(self, stones):
        if stones[1] != 1:
            return False

        n = len(stones)
        if n == 2:
            return True

        pos = dict(zip(stones, range(n)))
        dp = defaultdict(set)
        dp[1].add(1)

        for i in range(1, n):
            for k in dp[i]:
                for step in (k-1, k, k+1):
                    if step > 0 and stones[i]+step in pos:
                        nxt = pos[stones[i]+step]
                        dp[nxt].add(step)
        
        return bool(dp[n-1])

# Unit Test
stones = [0,1,3,5,6,8,12,17]
sol = Solution()
assert sol.canCross(stones) == True
