from typing import List

class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        lo = 1
        hi = max(piles)

        while lo < hi:
            mid = lo + (hi - lo) // 2
            hours = sum((x + mid - 1) // mid for x in piles)

            if hours > h:
                lo = mid + 1
            else:
                hi = mid

        return lo
