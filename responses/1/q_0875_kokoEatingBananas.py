class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        def canFinish(piles, speed, h):
            hours = 0
            for p in piles:
                hours += (p + speed - 1) // speed
            return hours <= h

        left, right = 1, max(piles)
        while left < right:
            mid = left + (right - left) // 2
            if canFinish(piles, mid, h):
                right = mid
            else:
                left = mid + 1
        return left