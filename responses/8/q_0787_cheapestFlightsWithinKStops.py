from typing import List

class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
        INF = float('inf')

        distance = [INF] * n
        distance[src] = 0

        for _ in range(k + 1):
            new_distance = list(distance)
            for flight in flights:
                u, v, w = flight
                new_distance[v] = min(new_distance[v], distance[u] + w)
            distance = new_distance

        return distance[dst] if distance[dst] < INF else -1
