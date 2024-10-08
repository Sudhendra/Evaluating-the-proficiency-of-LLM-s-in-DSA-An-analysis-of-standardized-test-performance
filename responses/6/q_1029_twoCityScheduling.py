from typing import List

class Solution:
    def twoCitySchedCost(self, costs: List[List[int]]) -> int:
        total_cost = 0
        n = len(costs) // 2
        diff_costs = [(a - b, a, b) for a, b in costs]
        diff_costs.sort()
        for i in range(n):
            total_cost += diff_costs[i][1] + diff_costs[i + n][2]
        return total_cost
