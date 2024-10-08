from typing import List

class Solution:
    def maxSatisfied(self, customers: List[int], grumpy: List[int], minutes: int) -> int:
        n = len(customers)
        satisfied = 0
        max_additional_satisfied = 0
        additional_satisfied = 0

        for i in range(n):
            if grumpy[i] == 0:
                satisfied += customers[i]
            else:
                additional_satisfied += customers[i]

            if i >= minutes:
                additional_satisfied -= grumpy[i - minutes] * customers[i - minutes]
            
            max_additional_satisfied = max(max_additional_satisfied, additional_satisfied)

        return satisfied + max_additional_satisfied

solution = Solution()
print(solution.maxSatisfied([1, 0, 1, 2, 1, 1, 7, 5], [0, 1, 0, 1, 0, 1, 0, 1], 3))  # Output: 16
