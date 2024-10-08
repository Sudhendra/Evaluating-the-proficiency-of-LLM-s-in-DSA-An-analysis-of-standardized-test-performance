class Solution:
    def arrangeCoins(self, n: int) -> int:
        left, right = 0, n
        while left <= right:
            mid = left + (right - left) // 2
            curr_sum = mid * (mid + 1) // 2
            if curr_sum == n:
                return mid
            elif curr_sum < n:
                left = mid + 1
            else:
                right = mid - 1
        return right