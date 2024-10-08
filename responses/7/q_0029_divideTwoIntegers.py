class Solution:
    def divide(self, dividend: int, divisor: int) -> int:
        if dividend == 0:
            return 0

        if (dividend < 0) != (divisor < 0):
            sign = -1
        else:
            sign = 1

        dividend = abs(dividend)
        divisor = abs(divisor)
        quotient = 0

        while dividend >= divisor:
            temp, multi = divisor, 1
            while dividend >= temp:
                dividend -= temp
                quotient += multi
                temp <<= 1
                multi <<= 1

        result = sign * quotient
        return min(max(-2**31, result), 2**31 - 1)
