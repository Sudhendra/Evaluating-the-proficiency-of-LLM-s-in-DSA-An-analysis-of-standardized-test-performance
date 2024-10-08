from typing import List

class Solution:
    def maxSatisfied(
        self, customers: List[int], grumpy: List[int], minutes: int
    ) -> int:
        n = len(customers)
        
        total_customers = 0
        for i in range(n):
            if grumpy[i] == 0:
                total_customers += customers[i]
        
        max_additional_customers = 0
        cur_additional_customers = 0
        for i in range(n):
            if grumpy[i] == 1:
                cur_additional_customers += customers[i]
            if i >= minutes and grumpy[i - minutes] == 1:
                cur_additional_customers -= customers[i - minutes]
            max_additional_customers = max(max_additional_customers, cur_additional_customers)
        
        return total_customers + max_additional_customers
