class Solution:
    def preimageSizeFZF(self, k: int) -> int:
        def trailing_zeroes(n):
            count = 0
            while n > 0:
                n //= 5
                count += n
            return count

        left, right = k, 5 * k
        while left < right:
            mid = left + (right - left) // 2
            zeroes = trailing_zeroes(mid)
            if zeroes == k:
                return 5
            elif zeroes < k:
                left = mid + 1
            else:
                right = mid
        return 0