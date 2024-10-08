class Solution:
    def mirrorReflection(self, p: int, q: int) -> int:
        def gcd(a, b):
            while b:
                a, b = b, a % b
            return a
        
        lcm = p * q // gcd(p, q)
        
        if lcm // p % 2 == 0:
            return 2
        elif lcm // q % 2 == 0:
            return 0
        else:
            return 1
