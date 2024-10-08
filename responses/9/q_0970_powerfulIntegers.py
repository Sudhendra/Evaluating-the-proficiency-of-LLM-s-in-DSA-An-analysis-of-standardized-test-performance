from typing import List

class Solution:
    
    def powerfulIntegers(self, x: int, y: int, bound: int) -> List[int]:
        powerful_integers = set()
        i = 0
        j = 0
        
        while x ** i + y ** j <= bound:
            while x ** i + y ** j <= bound:
                powerful_integers.add(x ** i + y ** j)
                if y == 1:
                    break
                j += 1
            if x == 1:
                break
            i += 1
            j = 0
        
        return list(powerful_integers)
