from typing import List

class Solution:
    def twoCitySchedCost(self, costs: List[List[int]) -> int:
        n = len(costs) // 2
        total_cost = 0
        diff_costs = []

        for a, b in costs:
            total_cost += a
            diff_costs.append(b - a)

        diff_costs.sort()
        for i in range(n):
            total_cost += diff_costs[i]

        return total_cost
