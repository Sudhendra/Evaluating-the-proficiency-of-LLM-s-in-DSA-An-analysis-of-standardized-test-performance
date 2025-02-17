from typing import List

class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
        INF = float('inf')
        dp = [INF] * n
        dp[src] = 0
        
        for _ in range(k + 1):
            new_dp = dp.copy()
            for flight in flights:
                u, v, w = flight
                new_dp[v] = min(new_dp[v], dp[u] + w)
            dp = new_dp
        
        return dp[dst] if dp[dst] < INF else -1
