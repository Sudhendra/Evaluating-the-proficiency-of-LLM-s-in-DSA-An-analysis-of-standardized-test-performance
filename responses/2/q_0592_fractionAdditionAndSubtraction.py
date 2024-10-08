class Solution:
    def fractionAddition(self, expression: str) -> str:
        import re
        from fractions import Fraction
        
        fractions = re.findall(r'[+-]?\d+/\d+', expression)
        result = sum(map(Fraction, fractions), Fraction(0, 1))
        
        return str(result.numerator) + '/' + str(result.denominator)