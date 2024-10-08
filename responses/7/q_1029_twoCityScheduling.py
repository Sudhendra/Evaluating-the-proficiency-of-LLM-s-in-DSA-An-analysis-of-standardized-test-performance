from typing import List

class Solution:
    def twoCitySchedCost(self, costs: List[List[int]]) -> int:
        n = len(costs) // 2
        total_cost = 0
        diff_costs = [(a - b, a, b) for a, b in costs]
        diff_costs.sort()

        for diff, a, b in diff_costs[:n]:
            total_cost += a
        for diff, a, b in diff_costs[n:]:
            total_cost += b

        return total_cost
