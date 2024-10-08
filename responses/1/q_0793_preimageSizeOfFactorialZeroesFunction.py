class Solution:
    def preimageSizeFZF(self, k: int) -> int:
        def count_zeroes(n):
            count = 0
            while n > 0:
                n //= 5
                count += n
            return count

        lo, hi = k, 5 * k + 1

        while lo < hi:
            mid = lo + (hi - lo) // 2
            num_zeroes = count_zeroes(mid)
            if num_zeroes < k:
                lo = mid + 1
            elif num_zeroes > k:
                hi = mid
            else:
                return 5

        return 0