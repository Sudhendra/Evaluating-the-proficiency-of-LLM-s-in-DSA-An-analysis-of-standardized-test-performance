class Solution:
    def findRotateSteps(self, ring: str, key: str) -> int:
        def dp(i, j):
            if (i, j) in memo:
                return memo[(i, j)]
            if j == len(key):
                return 0

            res = float('inf')
            for k in dic[key[j]]:
                move = abs(i - k)
                minStepsToMove = min(move, len(ring) - move)
                nextSteps = dp(k, j + 1)
                res = min(res, minStepsToMove + nextSteps + 1)
            
            memo[(i, j)] = res
            return res

        memo = {}
        dic = {}
        for i, c in enumerate(ring):
            if c not in dic:
                dic[c] = []
            dic[c].append(i)

        return dp(0, 0)
