class Solution:
    def baseNeg2(self, n: int) -> str:
        if n == 0:
            return "0"
        
        res = ""
        while n != 0:
            remainder = n % 2
            n = -(n // 2)
            
            if remainder < 0:  # If remainder is negative, add 2 to n and set remainder to 1
                remainder += 2
                n += 1

            res = str(remainder) + res
        
        return res
