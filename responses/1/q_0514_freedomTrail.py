class Solution:
    def findRotateSteps(self, ring: str, key: str) -> int:
        from collections import defaultdict
        dp = defaultdict(lambda: float('inf'))

        def get_distance(a: int, b: int, n: int) -> int:
            return min(abs(a - b), n - abs(a - b))

        n = len(ring)
        m = len(key)
        dp[(0, key[0])] = 0

        for i in range(m):
            for j in dp:
                if j[1] == key[i]:
                    for k in range(n):
                        dp[(i + 1, ring[k])] = min(dp[(i + 1, ring[k])], dp[j] + get_distance(k, j[0], n) + 1)
        
        return min([dp[(m, c)] for c in ring])
