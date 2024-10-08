class Solution:
    def mirrorReflection(self, p: int, q: int) -> int:
        while q % 2 == 0 and p % 2 == 0:
            p /= 2
            q /= 2
        return 1 if q % 2 == 0 else 0 if p % 2 != 0 else 2
