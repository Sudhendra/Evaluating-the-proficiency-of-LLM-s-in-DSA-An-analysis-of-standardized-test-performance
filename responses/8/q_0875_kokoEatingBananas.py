from typing import List

class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        def can_finish(piles, h, k):
            hours = 0
            for pile in piles:
                hours += (pile + k - 1) // k
            return hours <= h

        left, right = 1, max(piles)
        while left < right:
            mid = left + (right - left) // 2
            if not can_finish(piles, h, mid):
                left = mid + 1
            else:
                right = mid
        return left