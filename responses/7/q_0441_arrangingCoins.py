class Solution:
    def arrangeCoins(self, n: int) -> int:
        low, high = 0, n
        while low <= high:
            mid = low + (high - low) // 2
            current = mid * (mid + 1) // 2
            if current == n:
                return mid
            elif current < n:
                low = mid + 1
            else:
                high = mid - 1
        return high
