class Solution:
    def convertToBase7(self, num: int) -> str:
        if num == 0:
            return "0"
        
        res = ""
        neg = num < 0
        num = abs(num)
        
        while num:
            res = str(num % 7) + res
            num //= 7
        
        if neg:
            res = "-" + res
        
        return res
