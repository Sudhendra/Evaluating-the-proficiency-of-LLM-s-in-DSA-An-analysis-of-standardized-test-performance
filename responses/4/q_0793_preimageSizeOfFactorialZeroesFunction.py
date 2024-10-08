class Solution:
    def preimageSizeFZF(self, k: int) -> int:
        def count_zeroes(n):
            count = 0
            while n > 0:
                n //= 5
                count += n
            return count

        left, right = 0, 5*k
        while left < right:
            mid = left + (right - left) // 2
            mid_zeroes = count_zeroes(mid)
            if mid_zeroes < k:
                left = mid + 1
            elif mid_zeroes > k:
                right = mid
            else:
                return 5

        return 0
