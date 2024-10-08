class Solution:
    def divide(self, dividend: int, divisor: int) -> int:
        INT_MIN, INT_MAX = -2**31, 2**31 - 1
        if dividend == 0:
            return 0
        if divisor == 1:
            return min(max(dividend, INT_MIN), INT_MAX)
        if divisor == -1:
            return min(max(-dividend, INT_MIN), INT_MAX)

        positive = (dividend > 0) is (divisor > 0)
        dividend, divisor = abs(dividend), abs(divisor)
        
        result = 0
        while dividend >= divisor:
            temp, i = divisor, 1
            while dividend >= temp:
                dividend -= temp
                result += i
                i <<= 1
                temp <<= 1
        
        if not positive:
            result = -result
        
        return min(max(result, INT_MIN), INT_MAX)
