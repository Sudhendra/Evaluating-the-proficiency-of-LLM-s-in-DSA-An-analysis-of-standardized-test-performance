from typing import List

class Solution:
    def shipWithinDays(self, weights: List[int], days: int) -> int:
        left, right = max(weights), sum(weights)
        
        while left < right:
            mid = left + (right - left) // 2
            current_weight = 0
            required_days = 1
            
            for weight in weights:
                if current_weight + weight > mid:
                    required_days += 1
                    current_weight = 0
                
                current_weight += weight
            
            if required_days > days:
                left = mid + 1
            else:
                right = mid
        
        return left
