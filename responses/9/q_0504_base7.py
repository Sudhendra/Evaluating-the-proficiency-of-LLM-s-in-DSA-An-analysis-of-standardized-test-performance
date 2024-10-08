class Solution:
    def convertToBase7(self, num: int) -> str:
        if num == 0:
            return "0"
        
        negative = num < 0
        num = abs(num)
        result = ""
        
        while num > 0:
            reminder = num % 7
            result = str(reminder) + result
            num //= 7
        
        if negative:
            result = "-" + result
        
        return result
