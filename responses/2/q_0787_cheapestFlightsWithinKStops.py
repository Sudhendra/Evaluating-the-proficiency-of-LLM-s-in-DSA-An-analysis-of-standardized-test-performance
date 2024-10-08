from typing import List

class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
        INF = 10**6
        dp = [[INF] * n for _ in range(k + 2)]
        dp[0][src] = 0

        for i in range(1, k + 2):
            dp[i][src] = 0
            for flight in flights:
                from_city, to_city, price = flight
                dp[i][to_city] = min(dp[i][to_city], dp[i - 1][from_city] + price)

        return dp[k + 1][dst] if dp[k + 1][dst] < INF else -1
