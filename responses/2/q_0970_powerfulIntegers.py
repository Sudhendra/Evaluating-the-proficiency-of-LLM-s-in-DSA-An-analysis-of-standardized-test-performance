class Solution:
    def powerfulIntegers(self, x: int, y: int, bound: int) -> List[int]:
        powerful_integers = set()
        bound_x = int(math.log(bound, x)) if x != 1 else 1
        bound_y = int(math.log(bound, y)) if y != 1 else 1
        
        for i in range(bound_x + 1):
            for j in range(bound_y + 1):
                val = x ** i + y ** j
                if val <= bound:
                    powerful_integers.add(val)
        
        return list(powerful_integers)