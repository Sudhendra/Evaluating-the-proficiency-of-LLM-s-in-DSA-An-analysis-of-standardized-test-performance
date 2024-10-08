from typing import List

class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        def can_eat_all(piles, k, h):
            hours = 0
            for bananas in piles:
                hours += bananas // k
                if bananas % k != 0:
                    hours += 1
                if hours > h:
                    return False
            return True
        
        left, right = 1, max(piles)
        
        while left < right:
            mid = (left + right) // 2
            if can_eat_all(piles, mid, h):
                right = mid
            else:
                left = mid + 1
        
        return left
