class Solution:
    def maxSatisfied(self, customers: List[int], grumpy: List[int], minutes: int) -> int:
        n = len(customers)
        satisfied_customers = 0
        max_extra_customers = 0
        extra_customers = 0
        for i in range(n):
            if grumpy[i] == 0:
                satisfied_customers += customers[i]
            else:
                extra_customers += customers[i]
            if i >= minutes:
                extra_customers -= grumpy[i - minutes] * customers[i - minutes]
            max_extra_customers = max(max_extra_customers, extra_customers)
        return satisfied_customers + max_extra_customers