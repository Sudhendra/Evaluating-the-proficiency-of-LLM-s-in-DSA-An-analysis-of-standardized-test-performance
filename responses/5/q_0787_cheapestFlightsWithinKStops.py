from typing import List

class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
        INF = 1e9
        dp = [INF] * n
        dp[src] = 0

        for _ in range(k + 1):
            new_dp = list(dp)
            for u, v, price in flights:
                new_dp[v] = min(new_dp[v], dp[u] + price)
            dp = new_dp

        return dp[dst] if dp[dst] < INF else -1
