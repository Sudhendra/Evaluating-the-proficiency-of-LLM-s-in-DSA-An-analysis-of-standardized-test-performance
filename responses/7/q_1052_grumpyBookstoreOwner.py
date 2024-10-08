from typing import List

class Solution:
    def maxSatisfied(self, customers: List[int], grumpy: List[int], minutes: int) -> int:
        satisfied_customers = 0
        max_additional_customers = 0
        additional_customers = 0

        for i in range(len(customers)):
            if grumpy[i] == 0:
                satisfied_customers += customers[i]
            else:
                additional_customers += customers[i]

            if i >= minutes:
                additional_customers -= grumpy[i - minutes] * customers[i - minutes]

            max_additional_customers = max(max_additional_customers, additional_customers)

        return satisfied_customers + max_additional_customers
