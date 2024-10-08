from math import gcd

class Solution:
    
    def fractionAddition(self, expression: str) -> str:
        def add_fraction(frac1, frac2):
            num1, den1 = map(int, frac1.split('/'))
            num2, den2 = map(int, frac2.split('/'))
            num = num1 * den2 + num2 * den1
            den = den1 * den2
            common = gcd(num, den)
            num //= common
            den //= common
            return f"{num}/{den}"
        
        fractions = expression.replace('+', ' +').replace('-', ' -').split()
        result = fractions[0]
        for i in range(1, len(fractions)):
            result = add_fraction(result, fractions[i])
        
        return result
