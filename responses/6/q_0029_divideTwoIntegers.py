class Solution:
    def divide(self, dividend: int, divisor: int) -> int:
        if dividend == 0:
            return 0

        if dividend == -2**31 and divisor == -1:
            return 2**31 - 1

        is_negative = (dividend < 0) != (divisor < 0)
        dividend, divisor = abs(dividend), abs(divisor)
        result = 0

        while dividend >= divisor:
            temp, multiple = divisor, 1
            while dividend >= temp:
                dividend -= temp
                result += multiple
                temp <<= 1
                multiple <<= 1

        if is_negative:
            result = -result

        return min(max(-2**31, result), 2**31 - 1)
