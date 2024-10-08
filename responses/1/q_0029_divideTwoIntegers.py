class Solution:
    def divide(self, dividend: int, divisor: int) -> int:
        INT_MIN, INT_MAX = -2**31, 2**31 - 1
        res = int(dividend / divisor)
        if res < INT_MIN:
            return INT_MIN
        elif res > INT_MAX:
            return INT_MAX
        else:
            return res