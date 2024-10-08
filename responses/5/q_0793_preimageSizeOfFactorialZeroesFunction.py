class Solution:
    def trailingZeroes(self, n: int) -> int:
        count = 0
        while n > 0:
            n //= 5
            count += n
        return count

    def preimageSizeFZF(self, k: int) -> int:
        lo, hi = k, 10*k + 1
        while lo < hi:
            mid = lo + (hi - lo) // 2
            zeros = self.trailingZeroes(mid)
            if zeros == k:
                return 5
            elif zeros < k:
                lo = mid + 1
            else:
                hi = mid
        return 0
