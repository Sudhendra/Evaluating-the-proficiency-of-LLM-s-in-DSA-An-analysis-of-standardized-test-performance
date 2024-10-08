class Solution:
    def powerfulIntegers(self, x: int, y: int, bound: int) -> List[int]:
        powerful_integers = set()
        for i in range(20):
            for j in range(20):
                val = x**i + y**j
                if val <= bound:
                    powerful_integers.add(val)
        return list(powerful_integers)
