class Solution:
    def divide(self, dividend: int, divisor: int) -> int:
        MAX_INT = 2**31 - 1
        MIN_INT = -2**31

        sign = 1 if (dividend < 0) == (divisor < 0) else -1
        dividend, divisor = abs(dividend), abs(divisor)

        quotient = 0
        while dividend >= divisor:
            temp, multiple = divisor, 1
            while dividend >= temp:
                dividend -= temp
                quotient += multiple
                multiple <<= 1
                temp <<= 1

        if sign == -1:
            quotient = -quotient

        return min(max(MIN_INT, quotient), MAX_INT)