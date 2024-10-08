class Solution:
    def gcd(self, a, b):
        while b:
            a, b = b, a % b
        return a
        
    def lcm(self, a, b):
        return a * b // self.gcd(a, b)
        
    def nthMagicalNumber(self, n: int, a: int, b: int) -> int:
        MOD = 10**9 + 7
        lcm_ab = self.lcm(a, b)
        
        def count(m):
            return m // a + m // b - m // lcm_ab

        left, right = 2, 10**18
        while left < right:
            mid = (left + right) // 2
            if count(mid) < n:
                left = mid + 1
            else:
                right = mid

        return left % MOD
