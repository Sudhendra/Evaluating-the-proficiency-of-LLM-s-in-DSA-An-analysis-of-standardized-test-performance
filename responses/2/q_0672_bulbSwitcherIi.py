class Solution:
    def flipLights(self, n: int, presses: int) -> int:
        if n == 0:
            return 1
        if n == 1:
            return min(2, presses + 1)
        if n == 2:
            return min(3, 1 << min(presses, 1))
        if presses == 1:
            return 4 if n == 3 else 7
        if presses == 2:
            return 7 if n == 3 else 8
        return 8
