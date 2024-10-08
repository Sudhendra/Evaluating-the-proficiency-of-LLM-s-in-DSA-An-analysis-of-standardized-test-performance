from typing import List

class Solution:
    def maxSatisfied(
        self, customers: List[int], grumpy: List[int], minutes: int
    ) -> int:
        n = len(customers)
        satisfied = 0
        max_satisfied = 0
        for i in range(n):
            if grumpy[i] == 0:
                satisfied += customers[i]
            customers[i] = customers[i] if grumpy[i] == 0 else 0

        for i in range(n):
            if i < minutes:
                satisfied += customers[i]

        max_satisfied = satisfied
        for i in range(n - minutes):
            satisfied = satisfied + customers[i + minutes] - customers[i]
            max_satisfied = max(max_satisfied, satisfied)

        return max_satisfied
