from typing import List

class Solution:
    def maxSatisfied(self, customers: List[int], grumpy: List[int], minutes: int) -> int:
        n = len(customers)
        satisfied = 0
        max_satisfied = 0
        for i in range(n):
            if grumpy[i] == 0:
                satisfied += customers[i]
        for i in range(minutes):
            if grumpy[i] == 1:
                satisfied += customers[i]
        max_satisfied = satisfied
        for i in range(minutes, n):
            if grumpy[i] == 1:
                satisfied += customers[i]
            if grumpy[i - minutes] == 1:
                satisfied -= customers[i - minutes]
            max_satisfied = max(max_satisfied, satisfied)
        return max_satisfied
