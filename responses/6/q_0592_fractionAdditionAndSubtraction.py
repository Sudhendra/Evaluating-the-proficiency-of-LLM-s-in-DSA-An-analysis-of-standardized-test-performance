from fractions import Fraction

class Solution:
    def fractionAddition(self, expression: str) -> str:
        total = sum(map(Fraction, expression.replace('-', ',-').split(',')))
        return str(total.numerator) + '/' + str(total.denominator)
