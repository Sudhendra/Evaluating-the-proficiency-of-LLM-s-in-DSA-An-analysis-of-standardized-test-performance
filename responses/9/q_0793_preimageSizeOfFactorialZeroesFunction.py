class Solution:
    def preimageSizeFZF(self, k: int) -> int:
        def countZeroes(n):
            res = 0
            while n:
                n //= 5
                res += n
            return res

        left, right = 0, k * 5
        while left < right:
            mid = (left + right) // 2
            numZeroes = countZeroes(mid)
            if numZeroes < k:
                left = mid + 1
            elif numZeroes > k:
                right = mid
            else:
                return 5  # 5 is the number of solutions for each k
        return 0
