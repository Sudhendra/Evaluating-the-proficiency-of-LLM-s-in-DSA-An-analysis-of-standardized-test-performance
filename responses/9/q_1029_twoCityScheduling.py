from typing import List

class Solution:
    def twoCitySchedCost(self, costs: List[List[int]]) -> int:
        n = len(costs) // 2
        total_cost = 0
        diff = []
        
        for cost in costs:
            diff.append(cost[0] - cost[1])
            total_cost += cost[1]
        
        diff.sort()
        for i in range(n):
            total_cost += diff[i]
        
        return total_cost
