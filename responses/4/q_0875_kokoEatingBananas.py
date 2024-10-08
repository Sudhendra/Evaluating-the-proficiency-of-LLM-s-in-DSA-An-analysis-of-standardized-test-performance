from typing import List

class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        left, right = 1, max(piles)  # Set the search space for k
        
        while left < right:
            mid = left + (right - left) // 2
            hours = sum((pile + mid - 1) // mid for pile in piles)  # Calculate hours needed with current eating speed
            
            if hours > h:  # Need more hours, increase eating speed
                left = mid + 1
            else:  # Hours needed is within limit, try lower eating speed
                right = mid
        
        return left
