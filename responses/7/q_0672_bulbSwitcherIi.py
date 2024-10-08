class Solution:
    def flipLights(self, n: int, presses: int) -> int:
        if presses == 0:
            return 1
        if n == 0:
            return 0
        if n == 1:
            return 2
        if n == 2:
            return min(3, 1 + (presses > 0))
        if n >= 3:
            if presses == 1:
                return 4
            if presses == 2:
                return 7
            return min(8, 1 + min(presses, 2))
