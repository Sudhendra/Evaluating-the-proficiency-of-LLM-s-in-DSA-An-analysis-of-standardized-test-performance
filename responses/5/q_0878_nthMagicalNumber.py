class Solution:
    def nthMagicalNumber(self, n: int, a: int, b: int) -> int:
        MOD = 10**9 + 7

        def gcd(x, y):
            while y:
                x, y = y, x % y
            return x
        
        def lcm(x, y):
            return x * y // gcd(x, y)

        LCM = lcm(a, b)

        def count_multiples_of_x(x):
            return x // a + x // b - x // LCM
        
        left = min(a, b)
        right = min(a, b) * n

        while left < right:
            mid = (left + right) // 2
            if count_multiples_of_x(mid) < n:
                left = mid + 1
            else:
                right = mid
                
        return left % MOD
