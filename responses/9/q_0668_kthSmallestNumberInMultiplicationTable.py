class Solution:
    def findKthNumber(self, m: int, n: int, k: int) -> int:
        def enough(x):
            count = 0
            for i in range(1, m + 1):
                count += min(x // i, n)
            return count >= k

        left, right = 1, m * n
        while left < right:
            mid = left + (right - left) // 2
            if not enough(mid):
                left = mid + 1
            else:
                right = mid

        return left
