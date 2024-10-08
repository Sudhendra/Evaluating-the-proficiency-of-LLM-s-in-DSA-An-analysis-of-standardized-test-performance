class Solution:
    def mirrorReflection(self, p: int, q: int) -> int:
        while p % 2 == 0 and q % 2 == 0:
            p, q = p // 2, q // 2
        return 1 if q % 2 == 1 and p % 2 == 0 else 0 if q % 2 == 1 else 2
