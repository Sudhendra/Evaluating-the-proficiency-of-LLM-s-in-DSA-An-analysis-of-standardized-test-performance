class Solution:
    def findKthNumber(self, m: int, n: int, k: int) -> int:
        def count_less_equal(x: int, m: int, n: int) -> int:
            count = 0
            for i in range(1, m + 1):
                count += min(x // i, n)
            return count

        left, right = 1, m * n
        while left < right:
            mid = left + (right - left) // 2
            if count_less_equal(mid, m, n) < k:
                left = mid + 1
            else:
                right = mid
        return left
