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
        
        hashmap = {}
        while remainder != 0:
            if remainder in hashmap:
                result.insert(hashmap[remainder], "(")
                result.append(")")
                break
            
            hashmap[remainder] = len(result)
            remainder *= 10
            result.append(str(remainder // denominator))
            remainder %= denominator
        
        return "".join(result)
