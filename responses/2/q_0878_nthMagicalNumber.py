class Solution:
    def nthMagicalNumber(self, n: int, a: int, b: int) -> int:
        def lcm(x, y):
            return x // math.gcd(x, y) * y
        
        mod = 10**9 + 7
        lcm_ab = lcm(a, b)
        left, right = min(a, b), n * min(a, b)

        while left < right:
            mid = (left + right) // 2
            magic_num = mid // a + mid // b - mid // lcm_ab

            if magic_num < n:
                left = mid + 1
            else:
                right = mid

        return left % mod