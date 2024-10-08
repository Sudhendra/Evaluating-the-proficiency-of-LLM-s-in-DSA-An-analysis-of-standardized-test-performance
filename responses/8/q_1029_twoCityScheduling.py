from typing import List

class Solution:
    def twoCitySchedCost(self, costs: List[List[int]) -> int:
        n = len(costs) // 2
        diff = [b - a for a, b in costs]
        diff.sort()
        return sum(a for a, _ in costs) + sum(diff[:n])

# The code logic for the "twoCitySchedCost" method has been implemented above.
