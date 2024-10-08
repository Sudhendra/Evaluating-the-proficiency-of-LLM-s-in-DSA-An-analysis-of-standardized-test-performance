class Solution:
    def preimageSizeFZF(self, k: int) -> int:
        def countZeroes(n):
            count = 0
            while n > 0:
                n //= 5
                count += n
            return count

        left, right = k, 10 * k + 1

        while left < right:
            mid = left + (right - left) // 2
            mid_zeroes = countZeroes(mid)

            if mid_zeroes == k:
                return 5
            elif mid_zeroes < k:
                left = mid + 1
            else:
                right = mid

        return 0
