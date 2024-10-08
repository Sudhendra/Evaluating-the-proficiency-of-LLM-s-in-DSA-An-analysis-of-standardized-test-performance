from typing import List

class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
        INF = float('inf')
        cost = [INF] * n
        cost[src] = 0

        for _ in range(k + 1):
            new_cost = cost.copy()
            for flight in flights:
                from_city, to_city, price = flight
                new_cost[to_city] = min(new_cost[to_city], cost[from_city] + price)
            cost = new_cost

        return cost[dst] if cost[dst] < INF else -1
