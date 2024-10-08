from fractions import Fraction

class Solution:
    def fractionAddition(self, expression: str) -> str:
        result = sum(map(Fraction, expression.replace('+', ' +').replace('-', ' -').split()))
        return str(result.numerator) + '/' + str(result.denominator)
