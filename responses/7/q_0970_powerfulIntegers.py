from typing import List

class Solution:
    def powerfulIntegers(self, x: int, y: int, bound: int) -> List[int]:
        powerful_integers = set()
        max_i = 20 if x == 1 else (31 - x.bit_length())
        max_j = 20 if y == 1 else (31 - y.bit_length())

        for i in range(max_i):
            for j in range(max_j):
                value = x ** i + y ** j
                if value <= bound:
                    powerful_integers.add(value)

                if y == 1:
                    break

            if x == 1:
                break

        return list(powerful_integers)
