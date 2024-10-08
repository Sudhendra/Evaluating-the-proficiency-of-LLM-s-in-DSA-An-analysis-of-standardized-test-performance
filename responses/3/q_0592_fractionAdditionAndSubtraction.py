from fractions import Fraction

class Solution:
    def fractionAddition(self, expression: str) -> str:
        if expression[0] != '-':
            expression = '+' + expression
        
        fractions = expression.replace('+', ' +').replace('-', ' -').split()
        total = sum(map(Fraction, fractions))
        
        return str(total.numerator) + '/' + str(total.denominator)
