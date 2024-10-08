class Solution:
    def flipLights(self, n: int, presses: int) -> int:
        n = min(n, 3)
        if presses == 0:
            return 1
        if n == 1:
            return 2
        if n == 2:
            return 3 if presses == 1 else 4
        if n == 3:
            return 7 if presses == 1 else 8 if presses == 2 else 8 if presses == 0 else 8
