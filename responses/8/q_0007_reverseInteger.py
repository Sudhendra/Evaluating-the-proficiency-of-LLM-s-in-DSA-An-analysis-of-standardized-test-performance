class Solution:
    def reverse(self, x: int) -> int:
        if x < 0:
            sign = -1
        else:
            sign = 1

        x = abs(x)
        result = 0
        
        while x != 0:
            digit = x % 10
            result = result * 10 + digit
            x //= 10
        
        result = sign * result
        
        if result < -2**31 or result > 2**31 - 1:
            return 0
        else:
            return result
