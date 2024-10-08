class Solution:
    def gcd(self, a, b):
        while b:
            a, b = b, a % b
        return a

    def lcm(self, a, b):
        return a * b // self.gcd(a, b)

    def nthMagicalNumber(self, n: int, a: int, b: int) -> int:
        MOD = 10**9 + 7

        def count_numbers_below_mid(mid):
            return mid // a + mid // b - mid // self.lcm(a, b)

        # Find the Least Common Multiple of a and b
        lcm_ab = self.lcm(a, b)

        # Binary search in [1, 10^18] range for the nth magical number
        lo, hi = 1, 10**18
        while lo < hi:
            mid = (lo + hi) // 2
            if count_numbers_below_mid(mid) < n:
                lo = mid + 1
            else:
                hi = mid

        return lo % MOD
