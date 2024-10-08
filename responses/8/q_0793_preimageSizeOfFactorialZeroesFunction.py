class Solution:
    def trailing_zeroes(self, n):
        count = 0
        while n >= 5:
            n //= 5
            count += n
        return count

    def preimageSizeFZF(self, k: int) -> int:
        left, right = 0, k*5
        while left < right:
            mid = (left + right) // 2
            if self.trailing_zeroes(mid) < k:
                left = mid + 1
            else:
                right = mid
        return 5 if self.trailing_zeroes(left) == k else 0
