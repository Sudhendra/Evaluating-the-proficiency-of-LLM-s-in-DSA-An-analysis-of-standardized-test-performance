class Solution:
    def fractionAddition(self, expression: str) -> str:
        from fractions import Fraction
        
        fractions = expression.replace('+', ' +').replace('-', ' -').split()
        total = sum(map(Fraction, fractions))
        
        return str(total.numerator) + '/' + str(total.denominator)