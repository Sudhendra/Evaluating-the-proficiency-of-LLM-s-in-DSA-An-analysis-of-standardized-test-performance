class Solution:
    def nthMagicalNumber(self, n: int, a: int, b: int) -> int:
        def gcd(x, y):
            while y:
                x, y = y, x % y
            return x

        lcm = a * b // gcd(a, b)
        mod = 10**9 + 7

        left, right = 2, min(a, b) * n

        while left < right:
            mid = (left + right) // 2
            if mid // a + mid // b - mid // lcm < n:
                left = mid + 1
            else:
                right = mid

        return left % mod