class Solution:
    def leastOpsExpressTarget(self, x: int, target: int) -> int:
        pos = [float('inf')] * 100
        neg = [float('inf')] * 100
        pos[0] = cost = x
        neg[0] = cost = 2*x
        for i in range(1, 100):
            pos[i] = min(i*x + pos[i-1], (i+1)*x + neg[i-1])
            neg[i] = min((2*i + 1)*x + pos[i-1], (2*i+2)*x + neg[i-1])
        
        dp = float('inf')
        for i in range(100):
            curr = min(i*x + pos[i-1], (i+1)*x + neg[i-1])
            dp = min(dp, curr)
        
        return dp + target - 1
