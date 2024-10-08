class Solution:
    def fractionToDecimal(self, numerator: int, denominator: int) -> str:
        if numerator % denominator == 0:
            return str(numerator // denominator)
        res = []
        
        if numerator * denominator < 0:
            res.append('-')
        
        numerator, denominator = abs(numerator), abs(denominator)
        res.append(str(numerator // denominator))
        res.append('.')
        
        numerator %= denominator
        seen = {}
        index = len(res)
        
        while numerator != 0:
            if numerator in seen:
                res.insert(seen[numerator], '(')
                res.append(')')
                break
            
            seen[numerator] = index
            numerator *= 10
            res.append(str(numerator // denominator))
            numerator %= denominator
            index += 1
        
        return ''.join(res)
