from math import gcd

class Solution:
    def fractionAddition(self, expression: str) -> str:
        def add_fraction(fraction1, fraction2):
            num1, den1 = map(int, fraction1.split('/'))
            num2, den2 = map(int, fraction2.split('/'))
            numerator = num1 * den2 + num2 * den1
            denominator = den1 * den2
            common = gcd(numerator, denominator)
            return '{}/{}'.format(numerator // common, denominator // common)

        result = '0/1'
        i = 0
        while i < len(expression):
            j = i + 1
            while j < len(expression) and expression[j] != '+' and expression[j] != '-':
                j += 1
            result = add_fraction(result, expression[i:j])
            i = j

        return result
