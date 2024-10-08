from typing import List

class Solution:
    def shipWithinDays(self, weights: List[int], days: int) -> int:
        def is_possible_capacity(weights, days, capacity):
            current_capacity = capacity
            required_days = 1

            for weight in weights:
                if weight > current_capacity:
                    current_capacity = capacity
                    required_days += 1
                current_capacity -= weight

            return required_days <= days

        left, right = max(weights), sum(weights)

        while left < right:
            mid = left + (right - left) // 2
            if is_possible_capacity(weights, days, mid):
                right = mid
            else:
                left = mid + 1

        return left
