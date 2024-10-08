from typing import List

class Solution:
    def shipWithinDays(self, weights: List[int], days: int) -> int:
        def is_possible(capacity):
            count = 1
            total_weight = 0
            for weight in weights:
                if total_weight + weight > capacity:
                    count += 1
                    total_weight = weight
                else:
                    total_weight += weight
            return count <= days

        left, right = max(weights), sum(weights)
        while left < right:
            mid = left + (right - left) // 2
            if is_possible(mid):
                right = mid
            else:
                left = mid + 1
        return left
