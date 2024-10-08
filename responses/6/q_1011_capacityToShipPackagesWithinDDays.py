from typing import List

class Solution:
    def shipWithinDays(self, weights: List[int], days: int) -> int:
        left, right = max(weights), sum(weights)
        while left < right:
            mid = (left + right) // 2
            if self.can_ship_in_days(weights, days, mid):
                right = mid
            else:
                left = mid + 1
        return left

    def can_ship_in_days(self, weights: List[int], days: int, capacity: int) -> bool:
        current_capacity = capacity
        needed_days = 1

        for weight in weights:
            if weight > current_capacity:
                needed_days += 1
                current_capacity = capacity
            current_capacity -= weight

        return needed_days <= days
