class Solution:
    def preimageSizeFZF(self, k: int) -> int:
        def trailing_zeroes(n):
            count = 0
            while n > 0:
                n //= 5
                count += n
            return count

        left, right = 0, 5 * k

        while left <= right:
            mid = (left + right) // 2
            if trailing_zeroes(mid) < k:
                left = mid + 1
            elif trailing_zeroes(mid) > k:
                right = mid - 1
            else:
                return 5

        return 0
