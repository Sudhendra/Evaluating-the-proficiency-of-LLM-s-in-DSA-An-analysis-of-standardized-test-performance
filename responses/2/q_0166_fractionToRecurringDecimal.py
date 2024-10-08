class Solution:
    def fractionToDecimal(self, numerator: int, denominator: int) -> str:
        if numerator == 0:
            return "0"
        
        result = []
        if (numerator < 0) ^ (denominator < 0):
            result.append("-")
        
        numerator, denominator = abs(numerator), abs(denominator)
        
        result.append(str(numerator // denominator))
        
        remainder = numerator % denominator
        if remainder == 0:
            return "".join(result)
        
        result.append(".")
        decimal_map = {}
        
        while remainder != 0:
            if remainder in decimal_map:
                result.insert(decimal_map[remainder], "(")
                result.append(")")
                break
            
            decimal_map[remainder] = len(result)
            digit = remainder * 10 // denominator
            result.append(str(digit))
            remainder = (remainder * 10) % denominator
        
        return "".join(result)