from typing import List

class Solution:

    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
        INF = 1e9
        dp = [INF] * n
        dp[src] = 0
        
        for _ in range(k+1):
            new_dp = list(dp)
            for flight in flights:
                from_city, to_city, price = flight
                new_dp[to_city] = min(new_dp[to_city], dp[from_city] + price)
            dp = new_dp
        
        return dp[dst] if dp[dst] != INF else -1
