class Solution:
    def nthMagicalNumber(self, n: int, a: int, b: int) -> int:
        def gcd(x, y):
            while y:
                x, y = y, x % y
            return x
        
        def lcm(x, y):
            return x * y // gcd(x, y)
        
        mod = 10**9 + 7
        low, high = min(a, b), n * min(a, b)
        
        while low < high:
            mid = (low + high) // 2
            count = mid // a + mid // b - mid // lcm(a, b)
            
            if count < n:
                low = mid + 1
            else:
                high = mid
        
        return low % mod
