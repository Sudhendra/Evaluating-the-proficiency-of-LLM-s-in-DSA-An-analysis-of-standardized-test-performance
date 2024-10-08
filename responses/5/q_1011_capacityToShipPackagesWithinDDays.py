from typing import List

class Solution:
    def shipWithinDays(self, weights: List[int], days: int) -> int:
        left, right = max(weights), sum(weights)

        while left < right:
            mid = left + (right - left) // 2
            total = 0
            required_days = 1

            for weight in weights:
                total += weight
                if total > mid:
                    required_days += 1
                    total = weight

            if required_days <= days:
                right = mid
            else:
                left = mid + 1

        return left
