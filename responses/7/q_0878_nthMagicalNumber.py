class Solution:
    def nthMagicalNumber(self, n: int, a: int, b: int) -> int:
        mod = 10 ** 9 + 7
        lcm_ab = a * b // math.gcd(a, b)

        def check(x):
            return x // a + x // b - x // lcm_ab

        left, right = 0, n * min(a, b)

        while left < right:
            mid = (left + right) // 2
            if check(mid) < n:
                left = mid + 1
            else:
                right = mid

        return left % mod
