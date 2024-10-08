class Solution:
    def convertToBase7(self, num: int) -> str:
        if num == 0:
            return "0"
        
        result = ""
        is_negative = False
        if num < 0:
            num = -num
            is_negative = True
        
        while num:
            result = str(num % 7) + result
            num //= 7
        
        if is_negative:
            result = "-" + result
        
        return result
