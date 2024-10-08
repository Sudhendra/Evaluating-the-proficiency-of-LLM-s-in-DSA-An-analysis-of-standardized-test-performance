from typing import List

class Solution:
    
    def powerfulIntegers(self, x: int, y: int, bound: int) -> List[int]:
        powerful_integers = set()
        x_power = 1
        while x_power < bound:
            y_power = 1
            while x_power + y_power <= bound:
                powerful_integers.add(x_power + y_power)
                if y == 1:
                    break
                y_power *= y
            if x == 1:
                break
            x_power *= x
        
        return list(powerful_integers)
