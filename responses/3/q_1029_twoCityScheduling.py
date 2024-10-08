from typing import List

class Solution:
    def twoCitySchedCost(self, costs: List[List[int]) -> int:
        n = len(costs) // 2
        costs.sort(key=lambda x: x[0] - x[1])
        total_cost = sum(cost[0] for cost in costs[:n]) + sum(cost[1] for cost in costs[n:])
        return total_cost
