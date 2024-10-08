class Solution:
    def reverse(self, x: int) -> int:
        if x >= 0:
            rev_x = int(str(x)[::-1])
        else:
            rev_x = -int(str(-x)[::-1])

        if rev_x < -2**31 or rev_x > 2**31 - 1:
            return 0
        return rev_x
