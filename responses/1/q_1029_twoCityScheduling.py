from typing import List

class Solution:
    def twoCitySchedCost(self, costs: List[List[int]]) -> int:
        n = len(costs) // 2
        total_cost = 0
        diff = []

        for a, b in costs:
            total_cost += a
            diff.append(b - a)
        
        diff.sort()
        for i in range(n):
            total_cost += diff[i]

        return total_cost