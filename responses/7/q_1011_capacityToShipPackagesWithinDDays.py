from typing import List

class Solution:
    def shipWithinDays(self, weights: List[int], days: int) -> int:
        left, right = max(weights), sum(weights)
        
        while left < right:
            mid = left + (right - left) // 2
            total = 0
            count = 1
            
            for weight in weights:
                if total + weight > mid:
                    count += 1
                    total = weight
                else:
                    total += weight
                
            if count > days:
                left = mid + 1
            else:
                right = mid
        
        return left
