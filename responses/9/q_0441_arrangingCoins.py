class Solution:
    def arrangeCoins(self, n: int) -> int:
        left, right = 0, n
        while left <= right:
            mid = left + (right - left) // 2
            curr = mid * (mid + 1) // 2
            if curr == n:
                return mid
            elif curr < n:
                left = mid + 1
            else:
                right = mid - 1
        return right
