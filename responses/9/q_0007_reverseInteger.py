class Solution:
    def reverse(self, x: int) -> int:
        if x == 0:
            return 0
        
        is_negative = x < 0
        x = abs(x)
        
        reversed_num = 0
        while x != 0:
            digit = x % 10
            x //= 10
            reversed_num = reversed_num * 10 + digit
            
        if is_negative:
            reversed_num *= -1
        
        if reversed_num < -2**31 or reversed_num > 2**31 - 1:
            return 0
        
        return reversed_num
