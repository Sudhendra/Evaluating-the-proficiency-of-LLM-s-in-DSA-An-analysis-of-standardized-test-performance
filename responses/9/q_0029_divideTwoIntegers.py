class Solution:
    def divide(self, dividend: int, divisor: int) -> int:
        sign = -1 if (dividend < 0) ^ (divisor < 0) else 1
      
        dividend = abs(dividend)
        divisor = abs(divisor)
      
        result = 0
        while dividend >= divisor:
            temp, multiple = divisor, 1
          
            while dividend >= (temp << 1):
                temp <<= 1
                multiple <<= 1
              
            dividend -= temp
            result += multiple
        
        result = min(max(-2**31, result * sign), 2**31 - 1)
      
        return result
