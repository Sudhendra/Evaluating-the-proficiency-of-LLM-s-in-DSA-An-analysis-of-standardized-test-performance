class Solution:
    def divide(self, dividend: int, divisor: int) -> int:
        INT_MIN, INT_MAX = -2**31, 2**31 - 1
        
        if dividend == 0:
            return 0
        
        if divisor == 1:
            return min(dividend, INT_MAX)
        
        if divisor == -1:
            if dividend == INT_MIN:
                return INT_MAX
            return max(-dividend, INT_MIN)
        
        sign = -1 if (dividend < 0) ^ (divisor < 0) else 1
        dividend, divisor = abs(dividend), abs(divisor)
        
        quotient = 0
        while dividend >= divisor:
            temp, count = divisor, 1
            while dividend >= temp:
                dividend -= temp
                quotient += count
                
                temp <<= 1
                count <<= 1
        
        if sign == -1:
            quotient = -quotient
        
        return min(max(INT_MIN, quotient), INT_MAX)
