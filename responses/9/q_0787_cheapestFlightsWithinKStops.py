front_matter = {
    "qid": 787,
    "title": "Cheapest Flights Within K Stops",
    "titleSlug": "cheapest-flights-within-k-stops",
    "difficulty": "Medium",
    "tags": [
        "Dynamic Programming",
        "Depth-First Search",
        "Breadth-First Search",
        "Graph",
        "Heap (Priority Queue)",
        "Shortest Path",
    ],
}
# ====================== DO NOT EDIT ABOVE THIS LINE ======================
from typing import List

class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
        INF = float('inf')
        dp = [0] + [INF] * (n-1)  # Initialize list for storing minimum prices

        for _ in range(k+1):
            dp_new = dp[:]  # Copy the current list for updating
            for f, t, p in flights:
                dp_new[t] = min(dp_new[t], dp[f] + p)
            dp = dp_new

        return dp[dst] if dp[dst] < INF else -1