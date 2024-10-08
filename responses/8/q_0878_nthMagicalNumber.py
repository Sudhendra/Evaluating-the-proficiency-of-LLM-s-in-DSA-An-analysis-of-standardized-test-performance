class Solution:
    def nthMagicalNumber(self, n: int, a: int, b: int) -> int:
        def gcd(x, y):
            while y:
                x, y = y, x % y
            return x

        def lcm(x, y):
            return x * y // gcd(x, y)

        MOD = 10**9 + 7
        lcm_ab = lcm(a, b)
        low, high = 0, 10**18

        while low < high:
            mid = (low + high) // 2
            count = mid // a + mid // b - mid // lcm_ab

            if count < n:
                low = mid + 1
            else:
                high = mid

        return low % MOD

# If you have multiple solutions, add them all here as methods of the same class.
