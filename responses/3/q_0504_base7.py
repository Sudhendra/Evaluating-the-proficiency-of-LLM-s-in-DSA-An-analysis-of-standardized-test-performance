class Solution:
    def convertToBase7(self, num: int) -> str:
        if num == 0:
            return "0"
        
        negative = False
        if num < 0:
            negative = True
            num = -num
        
        base_7 = ""
        while num > 0:
            remainder = num % 7
            base_7 = str(remainder) + base_7
            num //= 7
        
        return "-" + base_7 if negative else base_7