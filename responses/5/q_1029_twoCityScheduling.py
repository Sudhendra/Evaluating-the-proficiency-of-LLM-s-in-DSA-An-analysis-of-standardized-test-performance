from typing import List

class Solution:
    def twoCitySchedCost(self, costs: List[List[int]) -> int:
        n = len(costs) // 2
        diff_costs = [a - b for a, b in costs]
        sorted_costs = sorted((cost, i) for i, cost in enumerate(diff_costs))
        
        min_cost = 0
        for cost, i in sorted_costs[:n]:
            min_cost += costs[i][0]
        for cost, i in sorted_costs[n:]:
            min_cost += costs[i][1]
            
        return min_cost
