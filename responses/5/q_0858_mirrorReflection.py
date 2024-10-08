class Solution:
    def mirrorReflection(self, p: int, q: int) -> int:
        def gcd(a, b):
            return a if b == 0 else gcd(b, a % b)

        gcd_val = gcd(p, q)
        p = (p // gcd_val) % 2
        q = (q // gcd_val) % 2

        return 1 if p == 1 and q == 1 else 0 if p == 1 else 2
